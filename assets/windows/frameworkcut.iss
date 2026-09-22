; FrameWork Cut's Windows installer.
;
; Built by build-app.yml with Inno Setup from the staged folder the .msi
; is also made of, so the two ship the same files; this is the one a
; person double-clicks, and it puts FrameWork Cut in the Start menu and can take
; it out again. Everything it needs is handed in on the command line:
;
;   iscc /DVersion=0.2.3 /DArch=x64compatible /DSuffix=x86_64 ^
;        /DStage=C:\...\stage\Concat-0.2.3-windows-x86_64 /DOut=C:\...\stage ^
;        assets\windows\concat.iss
;
; Arch is Inno's own word for the machine: x64compatible for the x86_64
; build (which also installs on ARM PCs, under emulation), arm64 for the
; native one. Suffix is the bundle's word for it, which names the file.

#ifndef Version
  #error Version is required
#endif
#ifndef Arch
  #error Arch is required: x64compatible or arm64
#endif
#ifndef Suffix
  #error Suffix is required: x86_64 or aarch64
#endif
#ifndef Stage
  #error Stage is required: the staged folder to install
#endif
#ifndef Out
  #define Out "."
#endif

[Setup]
; One id for the life of the product, so an install over an older one is
; an upgrade and not a second copy.
AppId={{A4E17C92-6D3B-4F58-9A0E-3C71B8D45E20}
AppName=FrameWork Cut
AppVersion={#Version}
AppVerName=FrameWork Cut {#Version}
AppPublisher=FrameWork
AppPublisherURL=https://framework.shop
AppSupportURL=https://framework.shop/support
AppUpdatesURL=https://github.com/SultanAsa/framework-cut/releases
DefaultDirName={autopf}\FrameWork Cut
DefaultGroupName=FrameWork Cut
DisableProgramGroupPage=yes
LicenseFile=..\..\LICENSE
OutputDir={#Out}
OutputBaseFilename=FrameWorkCut-{#Version}-windows-{#Suffix}-setup
SetupIconFile=..\icons\frameworkcut.ico
UninstallDisplayIcon={app}\frameworkcut.ico
UninstallDisplayName=FrameWork Cut
Compression=lzma2/max
SolidCompression=yes
WizardStyle=modern
ArchitecturesAllowed={#Arch}
ArchitecturesInstallIn64BitMode={#Arch}
; For the user alone unless they ask for the machine: no prompt for an
; administrator to install a video editor into one's own account.
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "{#Stage}\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "..\icons\frameworkcut.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\FrameWork Cut"; Filename: "{app}\frameworkcut.exe"; IconFilename: "{app}\frameworkcut.ico"
Name: "{autodesktop}\FrameWork Cut"; Filename: "{app}\frameworkcut.exe"; IconFilename: "{app}\frameworkcut.ico"; Tasks: desktopicon

[Run]
Filename: "{app}\frameworkcut.exe"; Description: "{cm:LaunchProgram,FrameWork Cut}"; Flags: nowait postinstall skipifsilent
