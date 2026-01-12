#!/bin/bash

#if [[ $EUID != 0 ]]; then #kontrollon nese je user root apo jo
#	echo "Ju lutemi filloni si ROOT \"Perdoreni: su \" "
#	exit 1
#fi

while true; do
	echo "========================="
	echo "   USER MANAGEMENT TOOL  "
	echo "========================="
	echo " 1) Shtoni User"
	echo " 2) Fshini User"
	echo " 3) Listo User-at"
	echo " 4) Login i Fundit i User-it"
	echo " 5) Krijoni File"
	echo " 6) Krijoni Directory"
	echo " 7) Fshini File"
	echo " 8) Fshini Directory"
	echo " 9) Ndryshoni Emrin e File"
	echo "10) Ndryshoni Permissions e File"
	echo "11) Ndryshoni Kush Ka Akses Tek Directory"
	echo "q) Dilni"
	echo ""
	read -p "Zgjidhni nje opsion: " opsioni #merr input nga perdoruesi

	if [[ $opsioni == "1" || $opsioni == "2" && $EUID != 0 ]]; then #nese zgjedh opsionin 1 ose 2 kontrollon nese je user root apo jo
		echo "Per te shtuar ose fshire user ju lutemi filloni si ROOT \"Perdoreni: su \" "
		exit 1
	fi
	
	case $opsioni in
	
		1)
			read -p "Shenoni username per ta shtuar: " username
			if id "$username" &>/dev/null; then
				echo "Useri ekziston."
			else
				useradd "$username"
				passwd "$username"
				echo "User $username u krijua me sukses."
			fi
			;;
		2)
			read -p "Shenoni username qe deshironi te fshini: " username
			if id "$username" &>/dev/null; then
				userdel "$username"
				echo "Useri $username u fshi me sukses."
			else
				echo "Useri nuk ekziston."
			fi
			;;
		3)
			echo " ----- System Users -----"
			cut -d: -f1 /etc/passwd
			;;
		4)
			read -p "Shenoni username: " username
			if id "$username" &>/dev/null; then
				last "$username" | head -n 1
			else
				echo "Useri nuk ekziston."
			fi
			;;
		5)
			read -p "Shenoni emrin e file: " fname
			if [[ -f $(pwd)/"$fname" ]]; then
				echo "Kujdes file ekziston."
			else
				touch "$fname"
				echo "File u krijua me sukses."
			fi
			;;
		6)
			read -p "Shenoni emrin e directory: " dname
			if [[ -d $(pwd)/"$dname" ]]; then
				echo "Kujdes directory ekziston."
			else
				mkdir "$dname"
				echo "Directory u krijua me sukses."
			fi
			;;
		7)
			read -p "Shenoni emrin e file: " fname
			if [[ -f $(pwd)/"$fname" ]]; then
				rm "$fname"
				echo "File u fshi me sukses."
			else
				echo "File nuk ekziston."
			fi
			;;
		8)
			read -p "Shenoni emrin e directory: " dname
			if [[ -d $(pwd)/"$dname" ]]; then
				rm -rf "$dname"
				echo "Directory u fshi me sukses."
			else
				echo "Directory nuk ekziston."
			fi
			;;
		9)
			read -p "Shenoni emrin e file: " fname
			if [[ -f $(pwd)/"$fname" ]]; then
				read -p "Shenoni emrin e ri te file: " ffname
				mv "$fname" "$ffname"
				ls -la "$ffname"
			else
				echo "File nuk ekziston."
			fi
			;;
		10)
			echo -e "Read 4\nWrite 2\nExecute 1"
			read -p "Shenoni emrin e file: " fname
			if [[ -f $(pwd)/"$fname" ]]; then
				read -p "Shenoni numrat per permissions \"Shembull 744\" " akses
				chmod "$akses" "$fname"
				echo "Permissions i file u ndryshua me sukses."
				ls -la "$fname"
			else
				echo "File nuk ekziston."
			fi
			;;
		11)
			read -p "Shenoni emrin e directory: " dname
			if [[ -d $(pwd)/"$dname" ]]; then
				read -p "Shenoni user dhe grupin qe doni te jepni akses \"root:root\" " akses
				chown "$akses" "$dname"
				echo "Aksesi u ndryshua me sukses."
				ls-ld "$dname"
			else
				echo "Directory nuk ekziston."
			fi
			;;
		q)
			echo "Exiting..."
			exit 0
			;;
		*)
			echo "Zgjidhni nje opsion tjeter";;
	esac

	echo ""
	read -p "Shtypni Enter per te vazhduar..."
	clear
done
