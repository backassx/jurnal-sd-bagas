import os

user_name = os.getenv("APP_USER", "Guest")
app_env = os.getenv("APP_ENV", "Development")

if __name__ == "__main__":
    print("=== Versi 2.0 - Stabil ===")
    print(f"Halo {user_name}!")
    print(f"Environment: {app_env}")
    print("Aplikasi ini berjalan di dalam kontainer Docker.")