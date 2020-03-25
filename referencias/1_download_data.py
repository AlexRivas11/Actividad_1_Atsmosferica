# Bajar y leer un fichero CSV
# Fichero CSV: Intensidad de los puntos de medida de bicicletas (espiras electromagnéticas)
# Obtenido de : http://gobiernoabierto.valencia.es/es/data/

import urllib.request
import csv


def create_csv(out_file, ls_data):
    file_data = open(out_file, 'w')
    writer = csv.writer(file_data, delimiter=';')
    for line in ls_data:
        writer.writerow(line.split(';'))
    file_data.close()


def download_data(url):
    contents = urllib.request.urlopen(url).read()
    contents_str = contents.decode('utf-8')
    # create lines in a list
    ls_bici = contents_str.split('\n')
    return ls_bici


if __name__ == "__main__":
    url_data = 'http://apigobiernoabiertortod.valencia.es/apirtod/rest/datasets/intensidad_espiras.csv '
    name_file_out = './intensidad_bicis.csv'
    ls_bicis = download_data(url_data)
    create_csv(out_file=name_file_out, ls_data=ls_bicis)
    print("Finish script...")

