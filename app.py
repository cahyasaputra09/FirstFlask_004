from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Parsing parameter dari form
        nama = request.form.get('nama')
        umur = request.form.get('umur')

        # Validasi input
        if nama and umur:
            try:
                umur = int(umur)
                result = f"Halo {nama}, umur Anda adalah {umur} tahun"
            except ValueError:
                result = "Umur harus berupa angka"
        else:
            result = "Silakan isi semua field"

    return render_template('index.html')

@app.route('/kelas2', methods=['GET', 'POST'])
def kelas2():
    message = None
    if request.method == 'POST':
        # Contoh form sederhana untuk kelas kedua
        hobi = request.form.get('hobi')
        if hobi:
            message = f"Hobi Anda adalah {hobi}"
        else:
            message = "Silakan isi hobi Anda!"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
