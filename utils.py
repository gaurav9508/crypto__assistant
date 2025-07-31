from dotenv import load_dotenv
import os
from pathlib import Path
import logging
import re

logger = logging.getLogger("crypto_assistant")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def load_env_vars():
    """
    Load environment variables from .env file with proper path detection
    """
    # Get the directory where utils.py is located
    current_dir = Path(__file__).parent
    
    # Look for .env file in the same directory as utils.py
    dotenv_path = current_dir / '.env'
    
    # If not found, try the parent directory (in case utils.py is in a subdirectory)
    if not dotenv_path.exists():
        dotenv_path = current_dir.parent / '.env'
    
    # If still not found, try current working directory
    if not dotenv_path.exists():
        dotenv_path = Path.cwd() / '.env'
    
    # Debug information
    print(f"Looking for .env file...")
    print(f"utils.py location: {current_dir}")
    print(f"Trying .env at: {dotenv_path}")
    print(f".env exists: {dotenv_path.exists()}")
    
    if not dotenv_path.exists():
        raise FileNotFoundError(f".env file not found. Searched in:\n"
                               f"1. {current_dir / '.env'}\n"
                               f"2. {current_dir.parent / '.env'}\n"
                               f"3. {Path.cwd() / '.env'}")
    
    # Load the .env file
    success = load_dotenv(str(dotenv_path))
    print(f"load_dotenv() success: {success}")
    
    # Get all environment variables
    env_vars = {
        'TELEGRAM_BOT_TOKEN': os.getenv('TELEGRAM_BOT_TOKEN'),
        'GEMINI_API_KEY': os.getenv('GEMINI_API_KEY'),
        'GOOGLE_CLOUD_PROJECT_ID': os.getenv('GOOGLE_CLOUD_PROJECT_ID'),
        'LOG_LEVEL': os.getenv('LOG_LEVEL', 'INFO'),
        'DEV_MODE': os.getenv('DEV_MODE', 'false'),
        'MAX_REQUESTS_PER_MINUTE': int(os.getenv('MAX_REQUESTS_PER_MINUTE', 30)),
        'MAX_AI_REQUESTS_PER_HOUR': int(os.getenv('MAX_AI_REQUESTS_PER_HOUR', 100)),
        'CACHE_TTL_SECONDS': int(os.getenv('CACHE_TTL_SECONDS', 300)),
        'ENABLE_CACHE': os.getenv('ENABLE_CACHE', 'true').lower() == 'true',
    }
    
    # Validate required variables
    required_vars = ['TELEGRAM_BOT_TOKEN', 'GEMINI_API_KEY']
    missing_vars = [var for var in required_vars if not env_vars[var]]
    
    if missing_vars:
        print("Environment variables found:")
        for key, value in env_vars.items():
            if value:
                if key in required_vars:
                    masked = f"{str(value)[:4]}...{str(value)[-4:]}" if len(str(value)) > 8 else "***"
                    print(f"  ✅ {key}: {masked}")
                else:
                    print(f"  ✅ {key}: {value}")
            else:
                print(f"  ❌ {key}: None")
        
        raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
    
    # Success message
    print("✅ All required environment variables loaded successfully!")
    
    return env_vars

def debug_environment():
    """Debug function to check environment setup"""
    print("=== ENVIRONMENT DEBUG ===")
    print(f"Current working directory: {os.getcwd()}")
    print(f"utils.py file location: {Path(__file__).parent}")
    
    # Check multiple possible .env locations
    possible_paths = [
        Path(__file__).parent / '.env',
        Path(__file__).parent.parent / '.env', 
        Path.cwd() / '.env'
    ]
    
    for i, path in enumerate(possible_paths, 1):
        print(f"\n{i}. Checking: {path}")
        print(f"   Exists: {path.exists()}")
        if path.exists():
            print(f"   Size: {path.stat().st_size} bytes")
            print(f"   Readable: {os.access(path, os.R_OK)}")
    
    print("=" * 40)

# def escape_markdown(text: str) -> str:
#     """
#     Escapes Telegram markdown special characters.
#     """
#     escape_chars = r'_*[]()~`>#+-=|{}.!'
#     return re.sub(f'([{re.escape(escape_chars)}])', r'\\\1', text)

def escape_markdown(text: str) -> str:
    # Escapes special characters for MarkdownV2
    escape_chars = r"_*[]()~`>#+-=|{}.!"
    return re.sub(f'([{re.escape(escape_chars)}])', r'\\\1', text)

if __name__ == "__main__":
    # Run debug when called directly
    debug_environment()
    try:
        env_vars = load_env_vars()
        print("Environment loading test successful!")
    except Exception as e:
        print(f"Environment loading test failed: {e}")