#!/usr/bin/env python3
# This example shows how to install forge and launch Minecraft using minecraft-launcher-lib
import minecraft_launcher_lib
import subprocess
import sys
import os


def ask_yes_no(text: str) -> bool:
    while True:
        answer = input(text + " [y|n] ")
        if answer.lower() == "y":
            return True
        elif answer.lower() == "n":
            return False
        else:
            print("Please enter y or n")


import minecraft_launcher_lib
import subprocess

def launch_minecraft(minecraft_directory, version, username):
    # Проверяем корректность входных данных
    print(f"Launching Minecraft with username: {username}, version: {version}")

    options = {
        "username": username,
        "uuid": "1234",  # Можно сгенерировать случайный UUID, если требуется уникальный идентификатор
        "token": "5678",  # Токен может быть пустым, если оффлайн-режим
        "version": version,
        "gameDirectory": minecraft_directory,
    }

    try:
        # Получаем команду запуска Minecraft
        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
            version, minecraft_directory, options
        )
        print(f"Generated command: {minecraft_command}")  # Логируем команду для отладки

        # Запускаем Minecraft с помощью subprocess
        result = subprocess.run(minecraft_command, capture_output=True, text=True)
        
        if result.returncode == 0:
            return f"Minecraft is launching as {username}..."
        else:
            return f"Failed to launch Minecraft. Error: {result.stderr}"
    
    except Exception as e:
        return f"Exception occurred: {e}"



def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == 'launch':
            version = sys.argv[2] 
            minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
            print(launch_minecraft(minecraft_directory, version))

        elif command == 'get_versions':
            print("\n".join(get_installed_versions()))

        else:
            print(install_forge(command))
    else:
        print("No command provided.")


def install_forge(vanilla_version):
    forge_version = minecraft_launcher_lib.forge.find_forge_version(vanilla_version)
    if forge_version is None:
        return "This Minecraft version is not supported by Forge."
    minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
    callback = {"setStatus": lambda text: print(text)}
    minecraft_launcher_lib.forge.install_forge_version(forge_version, minecraft_directory, callback=callback)
    return "Forge installed successfully."


def get_installed_versions():
    minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
    versions = minecraft_launcher_lib.utils.get_version_list(minecraft_directory)
    return [version['id'] for version in versions]

def main():
    print(f"Arguments received: {sys.argv}")  # Логируем аргументы

    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == 'launch':
            version = sys.argv[2]
            username = sys.argv[3]  # Читаем имя пользователя
            minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
            print(launch_minecraft(minecraft_directory, version, username))

        elif command == 'get_versions':
            print("\n".join(get_installed_versions()))

        else:
            print(install_forge(command))
    else:
        print("No command provided.")


if __name__ == "__main__":
    main()
