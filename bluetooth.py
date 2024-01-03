import subprocess
import bluetooth
import time

def yukle_bluetooth_modulu():
    try:
        subprocess.check_output(['sudo', 'apt-get', 'install', '-y', 'python3-bluez'])
        print("Bluetooth modülü başarıyla yüklendi.")
    except subprocess.CalledProcessError as e:
        print(f"Hata: Bluetooth modülü yüklenirken bir sorun oluştu. Hata kodu: {e.returncode}")

def bluetooth_baglan():
    yukle_bluetooth_modulu()

    while True:
        # Bluetooth cihazları tarayın
        cihazlar = bluetooth.discover_devices(duration=8, lookup_names=True, lookup_class=True, device_id=-1, device_name=False, device_class=False, device_oui=False, lookup_oui=False)

        if len(cihazlar) == 0:
            print("Yakındaki Bluetooth cihazları bulunamadı.")
            break

        print("Bulunan Bluetooth cihazları:")
        for addr, name, _ in cihazlar:
            print(f"{name} ({addr})")

            # Cihazlara bağlanma örneği
            soket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

            try:
                soket.connect((addr, 1))
                print(f"{addr} adresine başarıyla bağlandı.")
            except Exception as e:
                print(f"Bağlantı hatası: {e}")
            finally:
                soket.close()

            # Her cihaz için 5 milisaniye bekleme
            time.sleep(0.005)

if __name__ == "__main__":
    bluetooth_baglan()
