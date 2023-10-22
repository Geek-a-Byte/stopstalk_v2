from flask import Flask, jsonify
from flask_cors import CORS
import scrapers
from scrapers import cses, codeforces, hackerrank, leetcode, lightoj, spoj, timus, uva, toph, atcoder,vjudge

links = [
    {'oj':'cses','text': cses.cses_username, 'url': cses.cses_url, 'solve_count': int(cses.cses)},
    {'oj':'lightoj','text': lightoj.loj_username, 'url': lightoj.loj_url, 'solve_count':  int(lightoj.loj)},
    {'oj':'leetcode','text': leetcode.lc_user, 'url': 'https://leetcode.com/'+leetcode.lc_user, 'solve_count': int(leetcode.leetcode)},
    {'oj':'hackerrank','text':  hackerrank.payload['username'], 'url': 'https://www.hackerrank.com/'+hackerrank.payload['username'], 'solve_count': int(hackerrank.total_count)},
    {'oj':'codeforces','text': codeforces.user, 'url': 'https://codeforces.com/profile/'+codeforces.user, 'solve_count':   int(codeforces.cf)},
    {'oj':'toph','text': toph.username, 'url': 'https://toph.co/u/'+toph.username, 'solve_count': int(toph.toph)},
    {'oj':'spoj','text': spoj.username, 'url': 'https://www.spoj.com/users/'+spoj.username, 'solve_count': int(spoj.spoj)},
    {'oj':'uva','text': uva.username, 'url': uva.profile_url, 'solve_count':  int(uva.uva)},
    {'oj':'timus','text': timus.id, 'url': timus.url, 'solve_count': int(timus.number)},
    # {'oj':'codechef','text':  codechef.username, 'url': codechef.url, 'solve_count': int(codechef.number)},
    {'oj':'atcoder','text': atcoder.username, 'url': atcoder.profile_url, 'solve_count':  int(atcoder.number)},
    {'oj':'vjudge','text': vjudge.username_2, 'url': 'https://vjudge.net/user/'+vjudge.username_2, 'solve_count': int(vjudge.number2)}
]

tot_all=0
for i in links:
    tot_all+=int(i['solve_count'])


# app instance
app = Flask(__name__)
CORS(app)

# /api/home
@app.route("/api/home", methods=['GET'])
def return_home():
    return jsonify({
        'total_solved': tot_all,
        'profile': links,
    })


if __name__ == "__main__":
    app.run(host ='0.0.0.0',debug=True, port=8085)
