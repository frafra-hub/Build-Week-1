import os
import requests
from datetime import datetime



# Lista dei verbi HTTP da testare, inclusi OPTIONS
def run_request(url):
    http_methods = ["OPTIONS", "GET", "POST", "PUT", "DELETE"]

    # Creazione della cartella dei log
    log_dir = "http_requests_logs"
    os.makedirs(log_dir, exist_ok=True)  # Crea la cartella se non esiste

    # Creazione del file di log con timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_path = os.path.join(log_dir, f"http_requests_log_{timestamp}.txt")

    # Creazione del file di log per questa sessione
    with open(log_file_path, "w") as log_file:
        log_file.write("== LOG DELLE RICHIESTE HTTP ==\n")
        log_file.write(f"URL testato: {url}\n\n")

    # Dizionario per salvare i risultati
    results = {}

    for method in http_methods:
        try:
            # Invia la richiesta corrispondente al metodo
            if method == "GET":
                response = requests.get(url)
            elif method == "POST":
                response = requests.post(url, data={"key": "value"})
            elif method == "PUT":
                response = requests.put(url, data={"key": "value"})
            elif method == "DELETE":
                response = requests.delete(url)
            elif method == "OPTIONS":
                response = requests.options(url)
            
            # Salvataggio del risultato
            results[method] = {
                "status_code": response.status_code,
                "reason": response.reason,
                "headers": dict(response.headers),
                "allowed_methods": response.headers.get("Allow", "Non specificati") if method == "OPTIONS" else "N/A"
            }
            
            # Preparazione del contenuto del log
            log_content = f"Metodo: {method}\n"
            log_content += f"Status Code: {response.status_code}\n"
            log_content += f"Reason: {response.reason}\n"
            log_content += f"Headers: {response.headers}\n"
            if method == "OPTIONS":
                log_content += f"Allowed Methods: {results[method]['allowed_methods']}\n"
            log_content += "-" * 50 + "\n"

            # Aggiunta al file di log unico
            with open(log_file_path, "a") as log_file:
                log_file.write(log_content)
        
        except Exception as e:
            # Gestione degli errori
            error_content = f"Metodo: {method}\nErrore: {str(e)}\n"
            error_content += "-" * 50 + "\n"
            results[method] = {"error": str(e)}
            
            # Aggiunta dell'errore al file di log unico
            with open(log_file_path, "a") as log_file:
                log_file.write(error_content)
        

        return log_file_path




