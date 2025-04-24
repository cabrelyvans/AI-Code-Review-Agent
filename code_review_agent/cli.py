import argparse
from agent.analyzer import analyze_code, save_review

def main():
    parser = argparse.ArgumentParser(description="AI Code Review Agent")
    parser.add_argument("--file", required=True, help="Chemin vers le fichier Python à analyser")
    parser.add_argument("--mode", default="strict", help="Mode de prompt : strict, mentor, test_focus...")
    parser.add_argument("--provider", default="ollama", help="Nom du provider (pour l’instant, utiliser 'ollama')")
    parser.add_argument("--model", default="mistral", help="Nom du modèle utilisé (ex: mistral, mistral:7b, phi)")

    args = parser.parse_args()

    print(f"Analyse du fichier {args.file} avec le mode '{args.mode}' et le modèle '{args.model}'...\n")
    output = analyze_code(file_path=args.file, mode=args.mode, model=args.model)

    save_review(output)
    print("✅ Revue générée et sauvegardée dans reviews/review_output.md")

if __name__ == "__main__":
    main()
