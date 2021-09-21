$User = "NLC\Accounts"
$Pass = ConvertTo-SecureString -String "(RXIYu:~C!m" -AsPlainText -Force
$Credential = New-Object -TypeName "System.Management.Automation.PSCredential" -ArgumentList $User, $Pass
$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri http://Athena.nlc.com/PowerShell/ -Authentication Kerberos -Credential $Credential
Import-PSSession $Session

#$acc = Read-Host -Promt "What account would you like to disable?"

Set-CASMailbox -Identity "ttestd" -ActiveSyncEnabled $false