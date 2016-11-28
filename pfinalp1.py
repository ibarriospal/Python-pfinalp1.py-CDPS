#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import os.path 
import os
import sys
import subprocess
from lxml import etree
from subprocess import Popen

operaciones = [ "create", "start", "stop", "destroy", "-h","add","config" ]
parametros = ["0","1","2","3","4","5","6","7","s1","s2","s3","s4","s5","s6","s7"]
orden = ""
parametro = ""
parametro_num = 0;
servName = ""
ejecutar = False

# ************************************************************************************************************************************************
# *****														DECLARACION DE LAS FUNCIONES 												     *****

# ************************************************************************************************************************************************
# ************************************************************************************************************************************************
# ** FUNCION create(n) QUE CREA TANTAS MV COMO n PASADO; SINO SE PASA ANDA SE CREAN SIEMPRE POR DEFECTO c1 y lb, A PARTIR DE AHI s1,s2,s3,s4,s5 **
# ************************************************************************************************************************************************

def create(n):

	# Si no hemos introducido parametros nos crea por defecto c1 y lb
	if (n == 0):
		# Creamos ficheros COW y los ficheros XML de lb y c1

		os.system('qemu-img create -f qcow2 -b cdps-vm-base-p3.qcow2 lb.qcow2')
		os.system('cp plantilla-vm-p3.xml lb.xml')
		os.system('qemu-img create -f qcow2 -b cdps-vm-base-p3.qcow2 c1.qcow2')
		os.system('cp plantilla-vm-p3.xml c1.xml')

		# * PARA lb *

		# Cargamos el fichero XML de lb y obtenemos el nodo raíz
		tree = etree.parse('/mnt/tmp/pfinalp1/lb.xml')
		root = tree.getroot()
		# Guardamos en 'doc' el fichero XML que vas a toquetear
		doc = etree.ElementTree(root)
		# Buscamos y guardamos las etiquetas 'source' en el nodo /devices/disk y en el nodo /devices/interfaces 
		source_disk = root.find("./devices/disk/source")
		source_interface = root.find("./devices/interface/source")
		name = root.find("name")
		# Editamos name
		name.text = 'lb'
		# Editar ese valor de la etiqueta 
		source_disk.set("file", '/mnt/tmp/pfinalp1/lb.qcow2')
		# Editamos la bridge de LAN1
		source_interface.set("bridge", 'LAN1')
		# Editamos LAN2
		source_interface_2 = root.find("devices")
		# Creamos sub-instancias/sub-elementos de source_interface_2
		sub_interface_2 = etree.SubElement(source_interface_2, "interface", type='bridge')
		sub_source_2 = etree.SubElement(sub_interface_2, "source", bridge='LAN2')
		sub_model = etree.SubElement(sub_source_2, "model", type='virtio')

		outFile = open('lb.xml', 'w')
		doc.write(outFile)

		# * PARA c1 *

		# Cargamos el fichero XML de lb y obtenemos el nodo raíz
		tree = etree.parse('/mnt/tmp/pfinalp1/c1.xml')
		root = tree.getroot()
		# Guardamos en 'doc' el fichero XML que vas a toquetear
		doc = etree.ElementTree(root)
		# Buscamos y guardamos las etiquetas 'source' en el nodo /devices/disk y en el nodo /devices/interfaces 
		source_disk = root.find("./devices/disk/source")
		source_interface = root.find("./devices/interface/source")
		name = root.find("name")
		# Editamos name
		name.text = 'c1'
		# Editar ese valor de la etiqueta 
		source_disk.set("file", '/mnt/tmp/pfinalp1/c1.qcow2')
		# Editamos la bridge de LAN1
		source_interface.set("bridge", 'LAN1')

		outFile = open('c1.xml', 'w')
		doc.write(outFile)

		print "SE HA CREADO TODO PARA N=0"

	elif ((n >= 1) and (n <= 5)):
		# Creamos ficheros COW y los ficheros XML de lb y c1

		os.system('qemu-img create -f qcow2 -b cdps-vm-base-p3.qcow2 lb.qcow2')
		os.system('cp plantilla-vm-p3.xml lb.xml')
		os.system('qemu-img create -f qcow2 -b cdps-vm-base-p3.qcow2 c1.qcow2')
		os.system('cp plantilla-vm-p3.xml c1.xml')
		#os.system('qemu-img create -f qcow2 -b cdps-vm-base-p3.qcow2 s1.qcow2')
		#os.system('cp /plantilla-vm-p3.xml s1.xml')

		# * PARA lb *

		# Cargamos el fichero XML de lb y obtenemos el nodo raíz
		tree = etree.parse('/mnt/tmp/pfinalp1/lb.xml')
		root = tree.getroot()
		# Guardamos en 'doc' el fichero XML que vas a toquetear
		doc = etree.ElementTree(root)
		# Buscamos y guardamos las etiquetas 'source' en el nodo /devices/disk y en el nodo /devices/interfaces 
		source_disk = root.find("./devices/disk/source")
		source_interface = root.find("./devices/interface/source")
		name = root.find("name")
		# Editamos name
		name.text = 'lb'
		# Editar ese valor de la etiqueta 
		source_disk.set("file", '/mnt/tmp/pfinalp1/lb.qcow2')
		# Editamos la bridge de LAN1
		source_interface.set("bridge", 'LAN1')
		# Editamos LAN2
		source_interface_2 = root.find("devices")
		# Creamos sub-instancias/sub-elementos de source_interface_2
		sub_interface_2 = etree.SubElement(source_interface_2, "interface", type='bridge')
		sub_source_2 = etree.SubElement(sub_interface_2, "source", bridge='LAN2')
		sub_model = etree.SubElement(sub_source_2, "model", type='virtio')

		outFile = open('lb.xml', 'w')
		doc.write(outFile)

		# * PARA c1 *

		# Cargamos el fichero XML de lb y obtenemos el nodo raíz
		tree = etree.parse('/mnt/tmp/pfinalp1/c1.xml')
		root = tree.getroot()
		# Guardamos en 'doc' el fichero XML que vas a toquetear
		doc = etree.ElementTree(root)
		# Buscamos y guardamos las etiquetas 'source' en el nodo /devices/disk y en el nodo /devices/interfaces 
		source_disk = root.find("./devices/disk/source")
		source_interface = root.find("./devices/interface/source")
		name = root.find("name")
		# Editamos name
		name.text = 'c1'
		# Editar ese valor de la etiqueta 
		source_disk.set("file", '/mnt/tmp/pfinalp1/c1.qcow2')
		# Editamos la bridge de LAN1
		source_interface.set("bridge", 'LAN1')

		outFile = open('c1.xml', 'w')
		doc.write(outFile)

		# Si introducimos 1 nos crea s1
		if (n >= 1):

			# * PARA s1 *
			os.system('qemu-img create -f qcow2 -b cdps-vm-base-p3.qcow2 s1.qcow2')
			os.system('cp plantilla-vm-p3.xml s1.xml')

			# Cargamos el fichero XML de lb y obtenemos el nodo raíz
			tree = etree.parse('/mnt/tmp/pfinalp1/s1.xml')
			root = tree.getroot()
			# Guardamos en 'doc' el fichero XML que vas a toquetear
			doc = etree.ElementTree(root)
			# Buscamos y guardamos las etiquetas 'source' en el nodo /devices/disk y en el nodo /devices/interfaces 
			source_disk = root.find("./devices/disk/source")
			source_interface = root.find("./devices/interface/source")
			name = root.find("name")
			# Editamos name
			name.text = 's1'
			# Editar ese valor de la etiqueta 
			source_disk.set("file", '/mnt/tmp/pfinalp1/s1.qcow2')
			# Editamos la bridge de LAN1
			source_interface.set("bridge", 'LAN2')

			outFile = open('s1.xml', 'w')
			doc.write(outFile)

			print "SE HA CREADO TODO PARA N=1"

		# Si introducimos 2 nos crea ademas s2
		if (n >= 2):

			# * PARA s2 *
			os.system('qemu-img create -f qcow2 -b cdps-vm-base-p3.qcow2 s2.qcow2')
			os.system('cp plantilla-vm-p3.xml s2.xml')

			# Cargamos el fichero XML de lb y obtenemos el nodo raíz
			tree = etree.parse('/mnt/tmp/pfinalp1/s2.xml')
			root = tree.getroot()
			# Guardamos en 'doc' el fichero XML que vas a toquetear
			doc = etree.ElementTree(root)
			# Buscamos y guardamos las etiquetas 'source' en el nodo /devices/disk y en el nodo /devices/interfaces 
			source_disk = root.find("./devices/disk/source")
			source_interface = root.find("./devices/interface/source")
			name = root.find("name")
			# Editamos name
			name.text = 's2'
			# Editar ese valor de la etiqueta 
			source_disk.set("file", '/mnt/tmp/pfinalp1/s2.qcow2')
			# Editamos la bridge de LAN1
			source_interface.set("bridge", 'LAN2')

			outFile = open('s2.xml', 'w')
			doc.write(outFile)

			print "SE HA CREADO TODO PARA N=2"

		# Si introducimos 3 nos crea ademas s3
		if (n >= 3):

			# * PARA s3 *
			os.system('qemu-img create -f qcow2 -b cdps-vm-base-p3.qcow2 s3.qcow2')
			os.system('cp plantilla-vm-p3.xml s3.xml')

			# Cargamos el fichero XML de lb y obtenemos el nodo raíz
			tree = etree.parse('/mnt/tmp/pfinalp1/s3.xml')
			root = tree.getroot()
			# Guardamos en 'doc' el fichero XML que vas a toquetear
			doc = etree.ElementTree(root)
			# Buscamos y guardamos las etiquetas 'source' en el nodo /devices/disk y en el nodo /devices/interfaces 
			source_disk = root.find("./devices/disk/source")
			source_interface = root.find("./devices/interface/source")
			name = root.find("name")
			# Editamos name
			name.text = 's3'
			# Editar ese valor de la etiqueta 
			source_disk.set("file", '/mnt/tmp/pfinalp1/s3.qcow2')
			# Editamos la bridge de LAN1
			source_interface.set("bridge", 'LAN2')

			outFile = open('s3.xml', 'w')
			doc.write(outFile)

			print "SE HA CREADO TODO PARA N=3"

			# Si introducimos 4 nos crea ademas s4
		if (n >= 4):

			# * PARA s4 *
			os.system('qemu-img create -f qcow2 -b cdps-vm-base-p3.qcow2 s4.qcow2')
			os.system('cp plantilla-vm-p3.xml s4.xml')

			# Cargamos el fichero XML de lb y obtenemos el nodo raíz
			tree = etree.parse('/mnt/tmp/pfinalp1/s4.xml')
			root = tree.getroot()
			# Guardamos en 'doc' el fichero XML que vas a toquetear
			doc = etree.ElementTree(root)
			# Buscamos y guardamos las etiquetas 'source' en el nodo /devices/disk y en el nodo /devices/interfaces 
			source_disk = root.find("./devices/disk/source")
			source_interface = root.find("./devices/interface/source")
			name = root.find("name")
			# Editamos name
			name.text = 's4'
			# Editar ese valor de la etiqueta 
			source_disk.set("file", '/mnt/tmp/pfinalp1/s4.qcow2')
			# Editamos la bridge de LAN1
			source_interface.set("bridge", 'LAN2')

			outFile = open('s4.xml', 'w')
			doc.write(outFile)

			print "SE HA CREADO TODO PARA N=4"

		# Si introducimos 5 nos crea ademas s5
		if (n == 5):

			# * PARA s5 *
			os.system('qemu-img create -f qcow2 -b cdps-vm-base-p3.qcow2 s5.qcow2')
			os.system('cp plantilla-vm-p3.xml s5.xml')

			# Cargamos el fichero XML de lb y obtenemos el nodo raíz
			tree = etree.parse('/mnt/tmp/pfinalp1/s5.xml')
			root = tree.getroot()
			# Guardamos en 'doc' el fichero XML que vas a toquetear
			doc = etree.ElementTree(root)
			# Buscamos y guardamos las etiquetas 'source' en el nodo /devices/disk y en el nodo /devices/interfaces 
			source_disk = root.find("./devices/disk/source")
			source_interface = root.find("./devices/interface/source")
			name = root.find("name")
			# Editamos name
			name.text = 's5'
			# Editar ese valor de la etiqueta 
			source_disk.set("file", '/mnt/tmp/pfinalp1/s5.qcow2')
			# Editamos la bridge de LAN1
			source_interface.set("bridge", 'LAN2')

			outFile = open('s5.xml', 'w')
			doc.write(outFile)

			print "SE HA CREADO TODO PARA N=5"
	else:
		print "ERROR a la hora de introducir el numero del parametro"


####################funcion anadir un servidor nuevo



def add(nameServ):
			print "creating: maquina " +str(nameServ)
			os.system('qemu-img create -f qcow2 -b cdps-vm-base-p3.qcow2 s'+str(nameServ)+'.qcow2')
			os.system('cp plantilla-vm-p3.xml s'+str(nameServ)+'.xml')

			# Cargamos el fichero XML de lb y obtenemos el nodo raíz
			tree = etree.parse('/mnt/tmp/pfinalp1/s'+str(nameServ)+'.xml')
			root = tree.getroot()
			# Guardamos en 'doc' el fichero XML que vas a toquetear
			doc = etree.ElementTree(root)
			# Buscamos y guardamos las etiquetas 'source' en el nodo /devices/disk y en el nodo /devices/interfaces 
			source_disk = root.find("./devices/disk/source")
			source_interface = root.find("./devices/interface/source")
			name = root.find("name")
			# Editamos name
			name.text = "s"+str(nameServ)
			# Editar ese valor de la etiqueta 
			source_disk.set("file", '/mnt/tmp/pfinalp1/s'+str(nameServ)+'.qcow2')
			# Editamos la bridge de LAN1
			source_interface.set("bridge", 'LAN2')

			outFile = open('s'+str(nameServ)+'.xml', 'w')
			doc.write(outFile)

			print "starting: maquina s"+str(nameServ)

			maquina = "s"+str(nameServ)+".xml"
			print maquina
			maquina2 ="s"+str(nameServ)
			start2(maquina,maquina2)

#########################funcion lanzar el nuevo servidor añadido			

def start2(maquina,maquina2):
	
			os.system('sudo brctl addbr LAN1')
			os.system('sudo brctl addbr LAN2')
			os.system('sudo ifconfig LAN1 up ')
			os.system('sudo ifconfig LAN2 up')
			os.system('HOME=/mnt/tmp sudo virt-manager')
			os.system('sudo brctl addbr LAN1')
			os.system('sudo brctl addbr LAN2')
			os.system('sudo ifconfig LAN1 up ')
			os.system('sudo ifconfig LAN2 up')
			os.system('HOME=/mnt/tmp sudo virt-manager')
			print "break1"
			# Lanzamos s1
			os.system('sudo virsh define ' +maquina+' ')
			
			print "break2"

			os.system('sudo virsh start ' +maquina2)
			os.system('sudo virsh start ' +maquina2)
			print "break3"

			
			os.system("xterm -rv -sb -rightbar -fa  monospace -fs  10  -title '"+maquina2+"' -e  'sudo virsh console "+maquina2+"' &")	




#########################  funcion configurar servidor



def config(nameServ):
	#creamos el dir mnt dond mo9ntaremos las imagenres
	os.system("mkdir mnt")
	#montamos las imagenes

	os.system('sudo vnx_mount_rootfs -s -r s'+str(nameServ)+'.qcow2 mnt')

	os.system('sudo brctl addbr LAN1')
	os.system('sudo brctl addbr LAN2')
	os.system('sudo ifconfig LAN1 up ')
	os.system('sudo ifconfig LAN2 up')
	os.system('HOME=/mnt/tmp sudo virt-manager')



	os.system('sudo virsh define s'+str(nameServ)+'.xml ')

	maquina3 ="s"+str(nameServ)


	#cambiamos el archivo hostname

	outFile = open('/mnt/tmp/pfinalp1/mnt/etc/hostname', 'w')
	outFile.write(maquina3)
	outFile.close()

	#cambiamos el archivo hosts
	
	outFile2 = open('/mnt/tmp/pfinalp1/mnt/etc/hosts', 'w')
	outFile2.write("127.0.0.1       localhost")
	outFile2.write("127.0.1.1       "+maquina3)
	outFile2.write("The following lines are desirable for IPv6 capable hosts")
	outFile2.write("::1     localhost ip6-localhost ip6-loopback")
	outFile2.write("ff02::1 ip6-allnodes")
	outFile2.write("ff02::2 ip6-allrouters")
	outFile2.close()


	#lanzamos el servidor ya configurado

	os.system('sudo virsh start s'+str(nameServ))
	os.system('sudo virsh start s'+str(nameServ))
	
	os.system("xterm -rv -sb -rightbar -fa  monospace -fs  10  -title '"+maquina3+"' -e  'sudo virsh console "+maquina3+"' &")

	#Desmontamos la imagen
	os.system("sudo vnx_mount_rootfs -u mnt")
	



# ***************************************************************************************
# * FUNCION start() QUE INICIA LAS DIFERENTES MAQUINAS VIRTUALES (c1,lb,s1,s2,s3,s4,s5) *
# ***************************************************************************************


def start(n):

	if (n == 0):
		print "start: maquinas por defecto"

		os.system('sudo brctl addbr LAN1')
		os.system('sudo brctl addbr LAN2')
		os.system('sudo ifconfig LAN1 up ')
		os.system('sudo ifconfig LAN2 up')
		os.system('HOME=/mnt/tmp sudo virt-manager')

		# Arrancamos las de por defecto
		os.system('sudo virsh define c1.xml ')
		os.system('sudo virsh start c1 ')
		os.system('sudo virsh start c1 ')

		os.system('sudo virsh define lb.xml ')
		os.system('sudo virsh start lb ')
		os.system('sudo virsh start lb ')

		# Las lanzamos en otra terminal lb y c1 (las dos por defecto)
		os.system("xterm -rv -sb -rightbar -fa  monospace -fs  10 -title 'c1' -e  'sudo virsh console c1' &")
		os.system("xterm -rv -sb -rightbar -fa  monospace -fs  10  -title 'lb' -e  'sudo virsh console lb' &")

	elif ((n >= 1) and (n <= 5)):	

		os.system('sudo brctl addbr LAN1')
		os.system('sudo brctl addbr LAN2')
		os.system('sudo ifconfig LAN1 up ')
		os.system('sudo ifconfig LAN2 up')
		os.system('HOME=/mnt/tmp sudo virt-manager')

		print "start: maquinas por defecto"
		# Se vuelven a lanzar las dos MV por defecto: lb y c1
		os.system('sudo virsh define c1.xml ')
		os.system('sudo virsh start c1 ')
		os.system('sudo virsh start c1 ')

		os.system('sudo virsh define lb.xml ')
		os.system('sudo virsh start lb ')
		os.system('sudo virsh start lb ')

		# Las lanzamos en otra terminal lb y c1 (las dos por defecto)
		os.system("xterm -rv -sb -rightbar -fa  monospace -fs  10 -title 'c1' -e  'sudo virsh console c1' &")
		os.system("xterm -rv -sb -rightbar -fa  monospace -fs  10  -title 'lb' -e  'sudo virsh console lb' &")

		if (n >= 1):
			print "start: maquina1 s1"
			# Lanzamos s1
			os.system('sudo virsh define s1.xml ')
			os.system('sudo virsh start s1 ')
			os.system('sudo virsh start s1 ')
			os.system("xterm -rv -sb -rightbar -fa  monospace -fs  10  -title 's1' -e  'sudo virsh console s1' &")
		if (n >= 2):
			print "start: maquina1 s2"
			# Lanzamos s2
			os.system('sudo virsh define s2.xml ')
			os.system('sudo virsh start s2 ')
			os.system('sudo virsh start s2 ')
			os.system("xterm -rv -sb -rightbar -fa  monospace -fs  10  -title 's2' -e  'sudo virsh console s2' &")		
		if (n >= 3):
			print "start: maquina1 s3"
			# Lanzamos s3
			os.system('sudo virsh define s3.xml ')
			os.system('sudo virsh start s3 ')
			os.system('sudo virsh start s3 ')
			os.system("xterm -rv -sb -rightbar -fa  monospace -fs  10  -title 's3' -e  'sudo virsh console s3' &")
		if (n >= 4):
			print "start: maquina1 s4"
			# Lanzamos s4
			os.system('sudo virsh define s4.xml ')
			os.system('sudo virsh start s4 ')
			os.system('sudo virsh start s4 ')
			os.system("xterm -rv -sb -rightbar -fa  monospace -fs  10  -title 's4' -e  'sudo virsh console s4' &")
		if (n == 5):
			print "start: maquina1 s5"
			#Lanzamos s5
			os.system('sudo virsh define s5.xml ')
			os.system('sudo virsh start s5 ')
			os.system('sudo virsh start s5 ')
			os.system("xterm -rv -sb -rightbar -fa  monospace -fs  10  -title 's5' -e  'sudo virsh console s5' &")
	else:
		print "ERROR a la hora de introducir el numero del parametro"


# **********************************************************************
# ***** FUNCION stop() QUE APAGA LAS DIFERENTES MAQUINAS VIRTUALES *****
# **********************************************************************

def stop(n):

	if(n==0):
		os.system('sudo virsh shutdown c1')
		os.system('sudo virsh shutdown lb')
		print "Stopping c1 y lb..."
	if(n ==1):
		os.system('sudo virsh shutdown s1')
		print "Stopping s1..."
	if(n ==2):
		os.system('sudo virsh shutdown s2')
		print "Stopping s2..."
	if(n ==3):
		os.system('sudo virsh shutdown s3')
		print "Stopping s3..."
	if(n ==4):
		os.system('sudo virsh shutdown s4')
		print "Stopping s4..."
	if(n ==5):
		os.system('sudo virsh shutdown s5')
		print "Stopping s5..."
	if(n ==6):
		os.system('sudo virsh destroy c1')
		os.system('sudo virsh destroy lb')
		
		os.system('sudo virsh destroy s1')
		
		os.system('sudo virsh destroy s2')
	
		os.system('sudo virsh destroy s3')
		os.system('sudo virsh destroy s4')
		os.system('sudo virsh destroy s5')
		print "All serves destroyed"	


# *****************************************************************************
# ***** FUNCION destroy() QUE DESTRUYE LOS ARCHIVOS .qcow2 y .xml CREADOS *****
# *****************************************************************************

def destroy():
	c1x = '/mnt/tmp/pfinalp1/c1.xml'
	c1q= '/mnt/tmp/pfinalp1/c1.qcow2'
	lbx = '/mnt/tmp/pfinalp1/lb.xml'
	lbq= '/mnt/tmp/pfinalp1/lb.qcow2'
	s1x = '/mnt/tmp/pfinalp1/s1.xml'
	s1q= '/mnt/tmp/pfinalp1/s1.qcow2'
	s2x = '/mnt/tmp/pfinalp1/s2.xml'
	s2q= '/mnt/tmp/pfinalp1/s2.qcow2'
	s3x = '/mnt/tmp/pfinalp1/s3.xml'
	s3q= '/mnt/tmp/pfinalp1/s3.qcow2'
	s4x = '/mnt/tmp/pfinalp1/s4.xml'
	s4q= '/mnt/tmp/pfinalp1/s4.qcow2'
	s5x = '/mnt/tmp/pfinalp1/s5.xml'
	s5q= '/mnt/tmp/pfinalp1/s5.qcow2'
	mnt= '/mnt/tmp/pfinalp1/mnt'

	if os.path.exists(c1q):
		os.system('rm c1.qcow2 -f')
	if os.path.exists(c1x):
		os.system('rm c1.xml -f')
	if os.path.exists(lbq):
		os.system('rm lb.qcow2 -f')
	if os.path.exists(lbx):
		os.system('rm lb.xml -f')
	if os.path.exists(s1q):
		os.system('rm s1.qcow2 -f')
	if os.path.exists(s1x):
		os.system('rm s1.xml -f')
	if os.path.exists(s2q):
		os.system('rm s2.qcow2 -f')
	if os.path.exists(s2x):
		os.system('rm s2.xml -f')
	if os.path.exists(s3q):
		os.system('rm s3.qcow2 -f')
	if os.path.exists(s3x):
		os.system('rm s3.xml -f')
	if os.path.exists(s4q):
		os.system('rm s4.qcow2 -f')
	if os.path.exists(s4x):
		os.system('rm s4.xml -f')
	if os.path.exists(s5q):
		os.system('rm s5.qcow2 -f')
	if os.path.exists(s5x):
		os.system('rm s5.xml -f')
	if os.path.exists(mnt):
		os.system('rm -rf mnt ')


# ******************************************************************
# ***** FUNCION help() QUE NOS PROPORCIONA LA AYUDA DEL SCRIPT *****
# ******************************************************************

def help():
	print "**********************************************************************\n"
	print "** Bienvenido a la ayuda del comando pfinalp1 de la asignatura CDPS **\n"
	print "**********************************************************************\n"
	print "\n El uso del comando es: python pfinalp1.py <orden> <parametros> o python pfinalp1.py <orden>\n"
	print "\n <orden> --> La orden puede ser 'create' 'start' 'stop' 'destroy'\n"
	print "------> 'create' : para crear los ficheros .qcow2 de diferencias y de especificación XML de cada MV, así como los bridges que soportan las LAN del escenario.\n"
	print "------> 'start' : para arrancar las máquinas virtuales y mostrar su consola.\n"
	print "------> 'stop' : para parar las máquinas virtuales.\n"
	print "------> 'destroy' : para liberar el escenario, borrando todos los ficheros creados.\n"
	print "\n <parametros> --> Los parametros pueden ser '1' '2' '3' '4' '5', dependiendo de los servidores que queremos arrancar \n"


# *******************************
# ***** LECTURA DEL COMANDO *****
# *******************************

if len(sys.argv) == 2: #Si solo se define la orden sin introducir parametros
	# Guardamos la operacion a realizar
	orden = sys.argv[1]
	parametro = "0"
	# Guardamos en operacion 
	operacion = orden
	if operaciones.count(orden) == 1:
		ejecutar = True
		parametro_num = int(parametro)
else:
	print "Parametro incorrecto"
if len(sys.argv) == 3: # Si se define la orden y los parametros correctamente
	orden = sys.argv[1]
	parametro = sys.argv[2]
	#servName = sys.argv[2]
	if operaciones.count(orden):
		print (parametro)
	#	if parametros.count(servName):
	#		ejecutar = True
	#		servName = servName
	#		print "Va bien"
			#break
		if parametros.count(parametro):
			ejecutar = True
			parametro_num = int(parametro)
			print "Va bien"
		else:
			print "Parametro incorrecto"
	else:
		print "Orden no disponible"	
else:
	print "Para ejecutar el script debe definir una orden entre las posibles, para mas info opcion -h"

# Si el comando es correcto, comenzamos la ejecucion
if (ejecutar == True):
	if orden == "create":
		print "Se ejecuta el create"
		create(parametro_num)
	elif orden == "start":
		start(parametro_num)
	elif orden == "stop":
		stop(parametro_num)
	elif orden == "destroy":
		destroy()
	elif orden == "add":
		add(parametro_num)
	elif orden == "config":
		config(parametro_num)		
	elif orden == "-h":
		help()
	else:
		print "fallo comando"