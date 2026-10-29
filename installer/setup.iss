[Setup]
AppName=Apex ESP Source
AppVersion=0.4.2
DefaultDirName={autopf}\ApexESP
DefaultGroupName=Apex ESP
OutputBaseFilename=apex-esp-src-setup
Compression=lzma2
SolidCompression=yes

[Files]
Source: "dist\apex-esp\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\Apex ESP"; Filename: "{app}\apex-esp.exe"