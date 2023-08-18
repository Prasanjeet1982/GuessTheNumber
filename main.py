import random
from fastapi import FastAPI, HTTPException

app = FastAPI()

secret_number = random.randint(1, 100)
max_attempts = 10
attempts = 0

@app.get("/")
def read_root():
    return {"message": "Welcome to Guess the Number game!"}

@app.post("/guess/{user_guess}")
def guess_number(user_guess: int):
    global attempts

    if attempts >= max_attempts:
        raise HTTPException(status_code=400, detail="Sorry, you've reached the maximum number of attempts.")

    attempts += 1
    if user_guess < secret_number:
        return {"message": "Too low! Try again."}
    elif user_guess > secret_number:
        return {"message": "Too high! Try again."}
    else:
        return {"message": f"Congratulations! You guessed the number {secret_number} in {attempts} attempts."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
