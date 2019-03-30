from flask import Flask, render_template, request, session
import riot_app as ri
from passlib.hash import sha256_crypt as sha
import configparser as cf

config = cf.ConfigParser()
config.read('config.ini')

encrypted_pass = config['DEFAULT']['PASSWORD']
encrypted_user = config['DEFAULT']['USER']
port = config['DEFAULT']['PORT']
host = config['DEFAULT']['HOST']
tournieId = ""

blueTeam = []
redTeam = []

app = Flask(__name__)
app.secret_key = b'(0a$li*&$p]/nap993-1z[1'

@app.route('/', methods=['GET'])
def login():
    beta = ri.get_summoner_by_id('qFPc7K5DPBFildIkrWDXd4W0MfM9H8jW5S82nMfeDxGCrTe3')
    beta.rank = ri.get_summoner_rank('qFPc7K5DPBFildIkrWDXd4W0MfM9H8jW5S82nMfeDxGCrTe3')[0]
    print(beta.rank.__dict__)

    alpha = ri.get_summoner_by_id('zgzqdg9xeHXQ9zZpo4TeprEiQ8eRqWU0c7HVrdyR7FJEVno')
    alpha.rank = ri.get_summoner_rank('zgzqdg9xeHXQ9zZpo4TeprEiQ8eRqWU0c7HVrdyR7FJEVno')[0]
    print(alpha.__dict__, beta.__dict__)
    return render_template('tyler.html', t1 = alpha, moe = beta)


if __name__ == '__main__':
    app.run(debug=True, host=host, port=port)