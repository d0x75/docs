Seguir esses passos:

- Enable-WindowsOptionalFeature -online -FeatureName Microsoft-Windows-Subsystem-Linux

- reboot

- dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
- dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

- reboot
