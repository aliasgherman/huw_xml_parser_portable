import PySimpleGUI as sg
from app.modules.parserxml import *

def main():
    layout = [
        [sg.Text('Select Folder containing .xml.gz files'), sg.InputText(), sg.FolderBrowse(key='__INDIR__')],
        [sg.Text('Select Output Folder'), sg.InputText(), sg.FolderBrowse(key='__OUTDIR__')],
        [sg.Submit(), sg.Cancel()]
    ]
    window = sg.Window("Huawei Dump Parser - Portable v 0.01", layout=layout)

    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):
            break
        elif event in ('Submit'):
            p_x = ParserXML(CUSTOM_DATE_FILTER=values["__INDIR__"],
                            EXPORT_DB=True,
                            EXPORT_CSV=False,
                            DUMPDIR=values["__INDIR__"],
                            EXPORT_DIR=values["__OUTDIR__"],
                            merge_versions=True,
                            name="ParserGUI")
            window.close()
            p_x.run()
        else:
            print(event, values)



if __name__ == "__main__":
    main()