__author__ = 'perun'

import core.distribution as dist


if __name__ == '__main__':

    first_class = dist.Data()

    while True:
        print("""++++++++++OPTIONS++++++++++
                (1) - CREATE NETWORKS
                (2) - CREATE INTEREST MATRIX
                    (2.1) - VOICE
                    (2.2) - VIDEO
                    (2.3) - BEST EFFORT
                (3) - CHANGE INTEREST MATRIX
                    (3.1) - VOICE
                    (3.2) - VIDEO
                    (3.3) - BEST EFFORT
                (4) - PROCESS DATA
                (5) - SHOW DATA
                (6) - USE TEST VALUES
                (7) - SHOW INTEREST MATRIX
                (8) - DELETE NETWORK
                (9) - EXIT PROGRAM
                ++++++++++OPTIONS+++++++++++""")
        what = str(input('Your choice: '))

        if what == '1':
            print('Stwórz sieć: c - PSTN/ISDN/GSM; p - IP ')
            while str(input('Kontynuować? (y/n): ')) == 'y':

                mode = str(input('Podaj typ sieci: '))

                if mode == 'c':
                    first_class.create_circuit_network(int(input('Podaj intensywnosc: ')),
                                                       float(input('Podaj prawdopodobieństwo straty: ')))
                elif mode == 'p':
                    first_class.create_package_network(int(input('Podaj intensywnosc: ')))
                else:
                    print("Błędna wartość. Spróbuj ponownie.")
                    continue

        elif '2.' in what:
            if what == '2.1':
                first_class.create_interest_matrix(first_class.interest_matrix_voice)
            elif what == '2.2':
                first_class.create_interest_matrix(first_class.interest_matrix_video)
            elif what == '2.3':
                first_class.create_interest_matrix(first_class.interest_matrix_be)
            else:
                print('Wrong value! Choose from available options.')
            first_class.split_matrix()

        elif '3.' in what:
            row = str(input('Set row: '))
            col = str(input('Set column: '))
            if what == '3.1':
                first_class.change_single_value_matrix(row, col, first_class.interest_matrix_voice)
            elif what == '3.2':
                first_class.change_single_value_matrix(row, col, first_class.interest_matrix_video)
            elif what == '3.3':
                first_class.change_single_value_matrix(row, col, first_class.interest_matrix_be)
            else:
                print('Wrong value! Choose from available options.')

        elif what == '4':
            first_class.process_data()

        elif what == '5':
            first_class.show_data()

        elif what == '6':
            first_class.use_test_values()

        elif what == '7':
            print(first_class.interest_matrix_voice)
            print(first_class.interest_matrix_video)
            print(first_class.interest_matrix_be)

        elif what == '8':
            first_class.delete_network(int(input('Podaj indeks sieci, którą chcesz usunąć: ')))

        elif what == '9':
            print('EXIT PROGRAM')
            break