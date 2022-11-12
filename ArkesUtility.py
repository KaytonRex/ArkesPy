import os
import datetime
import json


def LoggingFile(LogType, LogMessage):
    # Creates the logging file structure
    ArkesFolder = os.getcwd()
    LoggingFolder = os.path.join(ArkesFolder, "Logging")
    CurrentDateTime = datetime.datetime.now()
    LoggingFile = os.path.join(LoggingFolder, f"{CurrentDateTime.year}-{CurrentDateTime.month}-{CurrentDateTime.day}.txt")
    LoggingLevel = "TRACE"
    LoggingPrint = True

    # Check if the folder and file exists, if fails, exit app
    LoggingFolderExists = os.path.exists(LoggingFolder)
    if not LoggingFolderExists:
        try:
            os.mkdir(LoggingFolder)
        except FileExistsError:
            LoggingFolderExists = True
        except (IOError, ValueError, EOFError) as e:
            print(f"{datetime.datetime.now()} \t Type: Error \t Process: Creating Log Folder ({str(LoggingFolder)}). Please fix this and try again! \n {e}")
            exit()

    LoggingFileExists = os.path.exists(LoggingFile)
    if not LoggingFileExists:
        try:
            log = open(LoggingFile,"w+")
            log.write(f"{datetime.datetime.now()} \t Type: Startup \t Process: Created Logging File {LoggingFile}")
            log.close()
        except (IOError, ValueError, EOFError) as e:
            print(f"{datetime.datetime.now()} \t Type: Error \t Process: Creating Log File {LoggingFile}. Please fix this and try again! \n {e}")

    LoggingEnabled = False
    if (LoggingLevel == "TRACE" and LogType == "TRACE") or (LoggingLevel == "TRACE" and LogType == "WARNING") or (LoggingLevel == "TRACE" and LogType == "ERROR"):
        LoggingEnabled = True
    elif (LoggingLevel == "WARNING" and LogType == "WARNING") or (LoggingLevel == "WARNING" and LogType == "ERROR"):
        LoggingEnabled = True
    elif (LoggingLevel == "ERROR" and LogType == "ERROR"):
        LoggingEnabled = True
    else:
        # Doesn't meet logging criteria
        LoggingEnabled = False

    if LoggingEnabled:
        try:
            log = open(LoggingFile,"w+")
            log.write(f"{datetime.datetime.now()} \t Type: {LogType} \t Process: {LogMessage}")
            log.close()
        except (IOError, ValueError, EOFError) as e:
            print(f"{datetime.datetime.now()} \t Type: Error \t Process: Creating Log File {LoggingFile}. Please fix this and try again! {e}")

    if LoggingEnabled and LoggingPrint:
        print(f"{datetime.datetime.now()} \t Type: {LogType} \t Process: {LogMessage}")

def FolderUtility(action, folderpath):
    if action == "CREATE":
        try:
            if not os.path.exists(folderpath):
                os.makedirs(folderpath)
            else:
                LoggingFile("WARNING",f"Creating Folder {folderpath}, this folder already exists!")
        except (IOError, ValueError, EOFError) as e:
            LoggingFile("ERROR",f"Creating Folder {folderpath}. Following error message reported: {e}")
    elif action == "CHECK":
        try:
            if os.path.exists(folderpath):
                return True
            else:
                return False
        except (IOError, ValueError, EOFError) as e:
            LoggingFile("ERROR",f"Checking Folder {folderpath}. Following error message reported: {e}")
    else:
        LoggingFile("ERROR",f"FolderUtility Function Issue, Invalid Action Type: {action}")

def FileUtility(action, filepath):
    if action == "CREATE":
        try:
            if not os.path.exists(filepath):
                file = open(filepath,"w")
                file.close()
            else:
                LoggingFile("WARNING",f"Creating File {filepath}. this file already exists!")
        except (IOError, ValueError, EOFError) as e:
            LoggingFile("ERROR",f"Creating File {filepath}. Following error message reported: {e}")
    elif action == "CHECK":
        try:
            if os.path.exists(filepath):
                return True
            else:
                return False
        except (IOError, ValueError, EOFError) as e:
            LoggingFile("ERROR",f"Checking File {filepath}. Following error message reported: {e}")
    elif action == "REMOVE":
        try:
            if FileUtility("CHECK",filepath):
                os.remove(filepath)
            else:
                LoggingFile("WARNING",f"Removing File {filepath}. this file doesn't exist!")
        except (IOError, ValueError, EOFError) as e:
            LoggingFile("ERROR",f"Removing File {filepath}. Following error message reported: {e}")
    else:
        LoggingFile("ERROR",f"FileUtility Function Issue, Invalid Action Type: {action}")
