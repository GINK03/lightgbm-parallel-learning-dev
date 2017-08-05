# LightGBM Parallel run pacakge for Linux 

## Now Dev
1. autodeploy. auto define ip by asinble like system
2. calurate machine leanring with multi machine 

## Setting Up Ansible
Ansibleという自動化ソフトウェアで、ノードにデータセットとLightGBMのバイナリをばら撒き、
並列で計算する必要があります。

### Install Ansible
ホスト（コントロールするノード）にAnsibleをインストールする
```console
$ sudo apt install ansible
```
ホストにsshpassを追加する
```console
$ sudo apt install sshpass
```
password認証がデフォルトでは通らないので、このようにするので、問題ない
/etc/ansible/ansible.cfgにここの編集を付け加える
```console
[ssh_connection]
ssh_args = -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null
```

### Setting Up Users
ユーザをホストと、クラスターノードの両方に作る
```console
$ sudo adduser ansible 
...
set password ****
```


