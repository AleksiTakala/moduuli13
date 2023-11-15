from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku')
def alkuluku():
    isPrime = False
    args = request.args
    luku = int(args.get("luku"))
    if luku == 1:
        print("Ei alkuluku")
    elif luku > 1:
        for i in range(2, luku):
            if (luku % i) == 0:
                print("ei alkuluku")
                break
        else:
            print("On alkuluku")
            isPrime = True
    else:
        print("Ei Alkuluku")
    vastaus={
        "Luku" : luku,
        "isPrime" : isPrime
    }
    return
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

