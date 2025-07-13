import os

class TempAnalyzer:
    def __init__(self):
        self.folders = {
            "Temp do Usuário": os.getenv('TEMP'),
            "Temp do Sistema": os.path.join(os.getenv('SystemRoot', 'C:\\Windows'), 'Temp'),
            "Prefetch": os.path.join(os.getenv('SystemRoot', 'C:\\Windows'), 'Prefetch')
        }

    def analyze_folder(self, path):
        total_size = 0
        total_files = 0

        if not path or not os.path.exists(path):
            return 0, 0

        for root, dirs, files in os.walk(path):
            for file in files:
                try:
                    fp = os.path.join(root, file)
                    total_size += os.path.getsize(fp)
                    total_files += 1
                except Exception:
                    pass  # ignora arquivos inacessíveis

        return total_files, total_size

    def analyze(self):
        results = {}
        total_files = 0
        total_size = 0

        for name, folder in self.folders.items():
            files, size = self.analyze_folder(folder)
            results[name] = (files, size)
            total_files += files
            total_size += size

        results["Total Geral"] = (total_files, total_size)
        return results

    def format_size(self, size_bytes):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_bytes < 1024:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.2f} PB"
