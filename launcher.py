import PySimpleGUI as sg
import os
from app.modules.parserxml import *


# def main():
#     layout = [
#         [
#             sg.Text("Select Folder containing .xml.gz files"),
#             sg.InputText(),
#             sg.FolderBrowse(key="__INDIR__"),
#         ],
#         [
#             sg.Text("Select Output Folder"),
#             sg.InputText(),
#             sg.FolderBrowse(key="__OUTDIR__"),
#         ],
#         [sg.Submit(), sg.Cancel()],
#     ]
#     window = sg.Window("Huawei Dump Parser - Portable v 0.01", layout=layout)

#     while True:
#         event, values = window.read()
#         if event in (None, "Cancel"):
#             break
#         elif event in ("Submit"):
#             p_x = ParserXML(
#                 CUSTOM_DATE_FILTER=values["__INDIR__"],
#                 EXPORT_DB=True,
#                 EXPORT_CSV=False,
#                 DUMPDIR=values["__INDIR__"],
#                 EXPORT_DIR=values["__OUTDIR__"],
#                 merge_versions=True,
#                 name="ParserGUI",
#             )
#             window.close()
#             p_x.run()
#         else:
#             print(event, values)


if __name__ == "__main__":
    # main()
    input_dir = "C:\\Users\\ALI.MANSOOR\\Downloads\\TEMP_DELETE\\Huawei MR Data 2025-06-15\\bsch04"
    output_dir = os.path.join(input_dir, "output")

    p_x = ParserXML(
        CUSTOM_DATE_FILTER="2025",
        EXPORT_DB=True,
        EXPORT_CSV=True,
        DUMPDIR=input_dir,
        EXPORT_DIR=output_dir,
        merge_versions=True,
        name="ParserGUI",
    )
    p_x.run()
