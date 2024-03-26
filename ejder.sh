#!/bin/bash

# Python dosyalarının bulunduğu dizini belirtin
python_dir="/data/data/com.termux/files/home/storage/downloads/ejderphisher"

# Python dosyalarını bul ve listele
python_files=($(ls -v "$python_dir"/*.py))
num_files=${#python_files[@]}

# Kullanıcıya seçenekleri göster
echo "Çalıştırmak istediğiniz Python dosyasını seçin:"
echo """
     Ben TURK HACK TEAM'den 3jd3rh4ck3r bu tool bana ait asla kimseye zarar vermeyin
  <==================================================================================>
                               (0)
                     
                dbdbdbdb        db   dbdbdb\    dbdbdbd   dbdbdb
                db              db   db    db   db        db   \\
                dbdbdb          db   db    db   dbdbdb    dbdbdb
                db              db   db    db   db        db    db
                dbdbdbdb   dbdbdb/   dbdbdb/    dbdbdbd   db    dbdb   
      
  <========================THT(TURK HACK TEAM) 3jd3rh4ck3r=======================>     
              BEN 3jd3rh4ck3r (TURK HACK TEAM'den tiktok hesabım 3jd3rh4ck3r
   __________________________________________________________________________________
    
      """
     


      
for ((i=0; i<num_files; i++)); do
    echo "$((i+1)). ${python_files[i]##*/}"
done

# Kullanıcıdan seçim al
echo toollu kapatmak için bire basın
read -p "Seçiminizi girin (1-7): " choice

# Seçilen dosyayı çalıştır
selected_file="${python_files[$((choice-1))]}"
echo "Seçilen dosya: $selected_file"
python3 "$selected_file"
