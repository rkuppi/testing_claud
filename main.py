class FibonacciGenerator:
    """A class to generate and manage Fibonacci series."""
    
    def __init__(self, n):
        """
        Initialize the FibonacciGenerator.
        
        Args:
            n (int): Number of terms in the Fibonacci series
        """
        self.n = n
        self.series = []
    
    def generate(self):
        """
        Generate the Fibonacci series.
        
        Returns:
            list: List containing Fibonacci series
        """
        if self.n <= 0:
            self.series = []
        elif self.n == 1:
            self.series = [0]
        else:
            self.series = [0, 1]
            for i in range(2, self.n):
                next_term = self.series[i-1] + self.series[i-2]
                self.series.append(next_term)
        
        return self.series
    
    def get_series(self):
        """Get the current Fibonacci series."""
        return self.series
    
    def display(self):
        """Display the Fibonacci series."""
        print(f"Fibonacci series with {self.n} terms:")
        print(self.series)


if __name__ == "__main__":
    # Example usage
    fib = FibonacciGenerator(10)
    fib.generate()
    fib.display()
