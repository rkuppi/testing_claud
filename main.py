def generate_fibonacci(n):
    """
    Generate Fibonacci series up to n terms.
    
    Args:
        n (int): Number of terms in the Fibonacci series
        
    Returns:
        list: List containing Fibonacci series
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_series = [0, 1]
    
    for i in range(2, n):
        next_term = fib_series[i-1] + fib_series[i-2]
        fib_series.append(next_term)
    
    return fib_series


if __name__ == "__main__":
    # Example usage
    num_terms = 10
    result = generate_fibonacci(num_terms)
    print(f"Fibonacci series with {num_terms} terms:")
    print(result)
