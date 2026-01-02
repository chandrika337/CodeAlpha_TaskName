from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    calc_result = ""
    palindrome_result = ""
    perfect_result = ""

    if request.method == "POST":
        print("Form data received:", request.form)

        # ---------- BODMAS CALCULATOR ----------
        expression = request.form.get("expression", "").strip()

        if expression:
            try:
                # Python evaluates expressions using BODMAS
                calc_result = eval(expression)
                print(f"BODMAS: {expression} = {calc_result}")
            except Exception as e:
                calc_result = f"Invalid Expression: {str(e)}"
                print(f"BODMAS Error: {e}")

        # ---------- PALINDROME CHECK (only if palnum is submitted) ----------
        palnum = request.form.get("palnum", "").strip()

        if palnum:
            try:
                num = int(palnum)

                # Palindrome check
                temp = num
                rev = 0
                while temp > 0:
                    rev = rev * 10 + temp % 10
                    temp //= 10

                if num == rev:
                    palindrome_result = f"{num} is a Palindrome Number"
                else:
                    palindrome_result = f"{num} is NOT a Palindrome Number"
                print(f"Palindrome: {palindrome_result}")
            except Exception as e:
                palindrome_result = f"Error: {str(e)}"
                print(f"Palindrome Error: {e}")

        # ---------- PERFECT NUMBER CHECK (only if perfnum is submitted) ----------
        perfnum = request.form.get("perfnum", "").strip()

        if perfnum:
            try:
                num = int(perfnum)
                
                if num > 0:
                    divisor_sum = 0
                    for i in range(1, num):
                        if num % i == 0:
                            divisor_sum += i

                    if divisor_sum == num:
                        perfect_result = f"{num} is a Perfect Number"
                    else:
                        perfect_result = f"{num} is NOT a Perfect Number"
                else:
                    perfect_result = "Error: Number must be positive"
                print(f"Perfect: {perfect_result}")
            except Exception as e:
                perfect_result = f"Error: {str(e)}"
                print(f"Perfect Error: {e}")

    return render_template(
        "index.html",
        calc_result=calc_result,
        palindrome_result=palindrome_result,
        perfect_result=perfect_result
    )

if __name__ == "__main__":
    import socket
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"\n{'='*60}")
    print(f"Starting Flask app")
    print(f"{'='*60}")
    print(f"🖥️  Desktop: http://127.0.0.1:5000")
    print(f"📱 Mobile:  http://{ip_address}:5000")
    print(f"{'='*60}\n")
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
