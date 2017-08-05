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

### Setting Up Users
ユーザをホストと、クラスターノードの両方に作る
```console
$ sudo adduser ansible 
...
set password ****
```


