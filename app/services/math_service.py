import httpx

class MathService:
    def get_properties(self, number: int) -> list:
        properties = []
        if self.is_armstrong(number):
            properties.append("armstrong")
        if number % 2 == 0:
            properties.append("even")
        else:
            properties.append("odd")

        return {
            "is_prime": self.is_prime(number),
            "is_perfect": self.is_perfect(number),
            "properties": properties,
            "digit_sum": self.digit_sum(number)
        }

    def is_armstrong(self, number: int) -> bool:
        digits = [int(d) for d in str(number)] # Convert number to list of digits
        return sum(d ** len(digits) for d in digits) == number # Check if the sum of the digits raised to the power of the number of digits is equal to the number
    
    
    def is_prime(self, number: int) -> bool:
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1): # Check divisibility up to the square root of the number
            if number % i == 0:
                return False
        return True

    def is_perfect(self, number: int) -> bool:
        if number < 2:
            return False
        return sum(i for i in range(1, number) if number % i == 0) == number

    def digit_sum(self, number: int) -> int:
        return sum(int(d) for d in str(number))


    async def get_fun_fact(self, number: int) -> str:
        url = f"http://numbersapi.com/{number}/math"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            return response.text