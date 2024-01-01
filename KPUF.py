import platform
import os
print('KPUF')
print('Create by ErkinKraft')
print('GitHub > https://github.com/ErkinKraft')
print()
def main():
    file_path = input("File>  ")

    if platform.system() == 'Windows':
        command = f'tasklist /FI "IMAGENAME eq {os.path.basename(file_path)}"'
    else:
        command = f'ps aux | grep {os.path.basename(file_path)}'

    process_info = os.popen(command).read()

    if process_info:
        print(f"Procces use file> {file_path}:")
        print(process_info)
        choice = input("Shutdown procces? (y/n): ")
        if choice.lower() == 'y':
            if platform.system() == 'Windows':
                os.system(f"taskkill /IM {os.path.basename(file_path)} /F")
            else:
                os.system(f"pkill -f {os.path.basename(file_path)}")
            print("Procces has been shutdown.")
        else:
            print("Procces shutdown.")
    else:
        print("Procces use file not found.")

if __name__ == "__main__":
    main()