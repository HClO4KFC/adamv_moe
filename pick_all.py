import os

def list_files(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.split('.')[-1] == 'py':
                if filename == 'pick_all.py':
                    continue
                file_path = os.path.join(dirpath, filename)
                # print(file_path)
                with open(file_path, 'r') as file:
                    func = '!!unknown function!!'
                    for line in file:
                        if 'def ' in line:
                            # print('==', line.split('def ')[-1].split('(')[0].strip())
                            # print()
                            func = line.split('def ')[-1].split('(')[0].strip()
                            print(line.strip())
                            pass
                        if 'gin.REQUIRED' in line:
                            # print(line.strip())
                            print(f'--{file_path}--{func}--{line.strip()}--')


if __name__ == '__main__':
    # base_dir = '/home/yhy/adamv_moe'
    base_dir = '.'
    list_files(base_dir)
