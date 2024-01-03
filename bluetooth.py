import subprocess
import bluetooth
import time

def yukle_bluetooth_modulu():
    try:
        subprocess.check_output(['sudo', 'apt-get', 'install', '-y', 'python3-bluez'])
        print("Bluetooth modÃ¼lÃ¼ baÅarÄ±yla yÃ¼klendi.")
    except subprocess.CalledProcessError as e:
        print(f"Hata: Bluetooth modÃ¼lÃ¼ yÃ¼klenirken bir sorun oluÅtu. Hata kodu: {e.returncode}")

def baslat_bluetooth():
    try:
        subprocess.check_output(['sudo', 'systemctl', 'start', 'bluetooth'])
        print("Bluetooth servisi baÅlatÄ±ldÄ±.")
    except subprocess.CalledProcessError as e:
        print(f"Hata: Bluetooth servisi baÅlatÄ±lÄ±rken bir sorun oluÅtu. Hata kodu: {e.returncode}")

def bluetooth_baglan():
    yukle_bluetooth_modulu()
    baslat_bluetooth()

    while True:
        # Bluetooth cihazlarÄ± tarayÄ±n
        try:
            cihazlar = bluetooth.discover_devices(duration=8, lookup_names=True, lookup_class=True, device_id=-1, device_name=False, device_class=False, device_oui=False, lookup_oui=False)
        except bluetooth.btcommon.BluetoothError as e:
            print(f"Hata: Bluetooth cihazlarÄ± tarama hatasÄ± - {e}")
            break

        if len(cihazlar) == 0:
            print("YakÄ±ndaki Bluetooth cihazlarÄ± bulunamadÄ±.")
            break

        print("Bulunan Bluetooth cihazlarÄ±:")
        for addr, name, _ in cihazlar:
            print(f"{name} ({addr})")

            # Cihazlara baÄlanma Ã¶rneÄi
            soket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

            try:
                soket.connect((addr, 1))
                print(f"{addr} adresine baÅarÄ±yla baÄlandÄ±.")
            except Exception as e:
                print(f"BaÄlantÄ± hatasÄ±: {e}")
            finally:
                soket.close()

            # Her cihaz iÃ§in 5 milisaniye bekleme
            time.sleep(0.005)

if __name__ == "__main__":
    bluetooth_baglan()