from datetime import date

def model_lead(name, email, company, stage):
    """Estrutura e modela um lead como dicionário"""
    return {
        "name": name,
        "email": email,
        "company": company,
        "stage": stage,
        "created": date.today().isoformat()
    }