# Creating an Image from the Snapshot of the Nginx Server and Launching a new Instance:

1. Instance launch ediyoruz(adı:SampleInstance) + resmin ip4 açıldığını kontrol et.
(standart seçimler, SHH-HTTP, t2.micro + user data kopyalayalım)
```bash
#!/bin/bash
yum update -y
amazon-linux-extras install nginx1.12
yum install wget -y
cd /usr/share/nginx/html
chmod o+w /usr/share/nginx/html
rm index.html
wget https://raw.githubusercontent.com/awsdevopsteam/route-53/master/index.html
wget https://raw.githubusercontent.com/awsdevopsteam/route-53/master/ken.jpg
systemctl start nginx
systemctl enable nginx
```

2. EBS seç, create snapshot->instance /oluşturduğumuz instance seç, tag name-value isim ver, create bas(ss-1).

3. Action menusunden-->Instance-Snapshot_First oluşan snapshot-> create image from snapshot tıkla ve içeriği default seç doldur. 
create image(AMI oluşturmuş olduk)

4. Soldan AMIs aç. -->launch instance from AMI'dan Instance_1_from_Sample_Instance oluştur ve yeni bir instance ayağa kaldır.

# Creating an Image and Launching an Instance from the same Image with "Action Menu":

1.  Go to SampleInstance

2.  Click the actions menu, Select image >> create image

3. Tag image and snapshots seperately->AMI ve snapshot (ss-2)yenileri oluştu.

4. AMI-2 aktif hale gelince, lauch instance from AMI tıklayıp Instance_2_from_Sample_Instance ayağa kaldırıyoruz.

# Creating an Image from the Snapshot of the Root Volume and Launching a new Instance:

1. sol menuden(EBS)Click create snapshot button

2. sample instance'dan ss-3 oluşturuyoruz.

3. AMI menuden create AMI-3

4. Launch instance as named "Instance_3_from_Sample_Instance(4.İNSTANCE OLUŞTU:))

# Make AMI public:

1. AMI menuden create AMI-4

2. Click on permission and Click on "Make public "

3. After a while it will be public. Send the AMI ID from slack

# Hosting WordPress on EC2 with AMI:

1. Create EC2 instance
2. AMI: AWS Marketplace : "WordPress Certified by Bitnami and Automattic" (Free tier) +  t2.micro + 10Gb is default + Tag : Key=Name, Value= WordPress + Sec.Grp : HTTP & HTTPS & SSH are default
3. Go to the browser and paste WP IP
4. to customize the page >>>>> after the IP add "/wp-admin"
5. instance tıkla-->Action >>> Monitor and Troubleshoot >>>>>> Get System logs >>>> "user name and password"
6. Go to browser and log in with credentials
7. delete WP instance:))

# Silme sırası(Delete all AMIs and Snapshots.);
---------------
1. instance, 
2. AMI(DEREGISTER),
3. SNAPSHOTS.