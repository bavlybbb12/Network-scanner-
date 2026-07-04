from flask import Flask, render_template, request
import scanner 
import utils 
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    target_subnet = utils.get_local_subnet()
    network_data = [] 
    
    if request.method == 'POST':
        user_input = request.form.get('subnet_input')
        if user_input:
            target_subnet = user_input 
            
        network_data = scanner.scan_network(target_subnet)
        utils.save_to_json(network_data)
        
    return render_template('index.html', devices=network_data, current_subnet=target_subnet)

if __name__ == '__main__':

    if not utils.is_admin():
        print("\n[!] ERROR: Missing Permissions")
        print("[-] This network scanner uses raw sockets and requires Administrator/Root privileges.")
        print("[*] Windows: Open your terminal or IDE as an 'Administrator' and try again.")
        print("[*] Linux/macOS: Run this script using 'sudo python app.py'.\n")
        
        # 2. Safely close the script with an error code (1)
        sys.exit(1)
        
    # 3. If they are admin, start the server!
    print("\n[+] Admin privileges confirmed. Starting local server...")
    app.run(debug=True)