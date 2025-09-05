# knowledge_base.py
"""
Knowledge Base for CompleteGPTOSSTutor
Separated for cleaner code and easier maintenance.
Each topic contains:
 - patterns: Regex patterns for matching queries
 - code: Example code block
 - explanation: Explanation of the concept
"""
        # Comprehensive knowledge base covering all major programming concepts
knowledge_base = {
            "oop_classes": {
                "patterns": [
                    r"class.*rectangle", r"rectangle.*class", r"oop.*class", r"python.*class",
                    r"object.*oriented", r"create.*class", r"method.*class", r"property.*class",
                    r"bank.*account", r"account.*class", r"simple.*class"
                ],
                "code": """```python
class BankAccount:
    \"\"\"Simple BankAccount class with deposit/withdraw functionality\"\"\"
    
    def __init__(self, account_holder: str, balance: float = 0.0):
        \"\"\"
        Initialize a BankAccount
        
        Args:
            account_holder: Name of the account holder
            balance: Initial balance (default: 0.0)
        \"\"\"
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_history = []
    
    def deposit(self, amount: float) -> None:
        \"\"\"Deposit money into account\"\"\"
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.transaction_history.append(f"Deposit: +${amount:.2f}")
    
    def withdraw(self, amount: float) -> None:
        \"\"\"Withdraw money from account\"\"\"
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transaction_history.append(f"Withdrawal: -${amount:.2f}")
    
    def get_balance(self) -> float:
        \"\"\"Get current balance\"\"\"
        return self.balance
    
    def get_statement(self) -> str:
        \"\"\"Get account statement\"\"\"
        statement = f"Account Holder: {self.account_holder}\\n"
        statement += f"Current Balance: ${self.balance:.2f}\\n"
        statement += "Transaction History:\\n"
        for transaction in self.transaction_history[-5:]:  # Last 5 transactions
            statement += f"  {transaction}\\n"
        return statement
    
    def __str__(self) -> str:
        return f"BankAccount(holder='{self.account_holder}', balance=${self.balance:.2f})"

# Example usage
if __name__ == "__main__":
    # Create bank account
    account = BankAccount("John Doe", 1000.0)
    
    # Perform transactions
    account.deposit(500.0)
    account.withdraw(200.0)
    account.deposit(300.0)
    
    print(account.get_statement())
    print(f"Current balance: ${account.get_balance():.2f}")
```""",
                "explanation": "Complete BankAccount class demonstrating object-oriented programming principles. Includes deposit/withdraw methods with validation, transaction history tracking, and proper error handling. Shows practical banking operations implementation."
            },
            "fibonacci": {
                "patterns": [
                    r"fibonacci", r"recursive.*function", r"recursion", r"sequence.*number",
                    r"calculate.*fib", r"fib.*number", r"recursive.*algorithm"
                ],
                "code": """```python
def fibonacci(n: int) -> int:
    \"\"\"Calculate Fibonacci number recursively\"\"\"
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Optimized version with memoization
def fibonacci_memo(n: int, memo: dict = None) -> int:
    \"\"\"Fibonacci with memoization for better performance\"\"\"
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# Iterative version (most efficient)
def fibonacci_iterative(n: int) -> int:
    \"\"\"Fibonacci using iterative approach\"\"\"
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Example usage and performance comparison
if __name__ == "__main__":
    print("Fibonacci Sequence (0-10):")
    print("Method\\t\\tResult\\t\\tTime Complexity")
    print("-" * 40)

    for i in range(11):
        fib_rec = fibonacci(i)
        fib_memo = fibonacci_memo(i)
        fib_iter = fibonacci_iterative(i)

        print(f"F({i})\\t\\t{fib_rec}\\t\\tO(2^n) - Exponential")
        # All methods should give same result
        assert fib_rec == fib_memo == fib_iter, "All methods should match"

    print("\\nPerformance Note:")
    print("• Recursive: Simple but exponential time complexity")
    print("• Memoized: Much faster, O(n) time and space")
    print("• Iterative: Most efficient, O(n) time, O(1) space")
```""",
                "explanation": "Complete Fibonacci implementation with three approaches: basic recursive (educational), memoized recursive (optimized), and iterative (most efficient). Includes performance analysis and validation checks."
            },
            "file_operations": {
                "patterns": [
                    r"read.*file", r"count.*lines", r"text.*file", r"file.*operation",
                    r"open.*file", r"process.*file", r"line.*count", r"file.*read"
                ],
                "code": """```python
def count_lines(filename: str) -> int:
    \"\"\"Count number of lines in a text file\"\"\"
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return -1
    except Exception as e:
        print(f"Error reading file: {e}")
        return -1

def read_file_lines(filename: str) -> list:
    \"\"\"Read all lines from a text file\"\"\"
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    except Exception as e:
        print(f"Error: {e}")
        return []

# Advanced file operations
def file_statistics(filename: str) -> dict:
    \"\"\"Get comprehensive file statistics\"\"\"
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        return {
            'total_lines': len(lines),
            'non_empty_lines': sum(1 for line in lines if line.strip()),
            'total_words': sum(len(line.split()) for line in lines),
            'total_chars': sum(len(line) for line in lines),
            'avg_line_length': sum(len(line) for line in lines) / len(lines) if lines else 0
        }
    except Exception as e:
        return {'error': str(e)}

# Write to file
def write_to_file(filename: str, content: str, mode: str = 'w') -> bool:
    \"\"\"Write content to a file\"\"\"
    try:
        with open(filename, mode, encoding='utf-8') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False

# Example usage
if __name__ == "__main__":
    filename = "sample.txt"
    
    # Create a sample file first
    sample_content = \"\"\"Hello World!
This is a sample text file.
It contains multiple lines.
Some lines are empty.

Like this one.
And this is the last line.\"\"\"
    
    write_to_file(filename, sample_content)
    
    # Test file operations
    line_count = count_lines(filename)
    if line_count >= 0:
        print(f"Number of lines: {line_count}")
    
    lines = read_file_lines(filename)
    print(f"Non-empty lines: {len(lines)}")
    
    stats = file_statistics(filename)
    print("File statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
```""",
                "explanation": "Comprehensive file operations including line counting, reading files, writing files, and gathering statistics. Includes proper error handling, UTF-8 encoding support, and practical examples."
            },
            "math_operations": {
                "patterns": [
                    r"max.*number", r"maximum.*number", r"find.*max", r"largest.*number",
                    r"min.*number", r"minimum.*number", r"find.*min", r"smallest.*number",
                    r"average.*number", r"mean.*number", r"math.*function", r"calculate.*number",
                    r"python.*function.*maximum", r"function.*find.*max",  # ADD THESE
                ],
                "code": """```python
def find_max(a: float, b: float, c: float) -> float:
    \"\"\"Find the maximum of three numbers\"\"\"
    return max(a, b, c)

def find_min(a: float, b: float, c: float) -> float:
    \"\"\"Find the minimum of three numbers\"\"\"
    return min(a, b, c)

def find_average(a: float, b: float, c: float) -> float:
    \"\"\"Calculate the average of three numbers\"\"\"
    return (a + b + c) / 3

# Additional math utilities
def math_operations(a: float, b: float, c: float) -> dict:
    \"\"\"Perform various math operations on three numbers\"\"\"
    numbers = [a, b, c]
    sorted_nums = sorted(numbers)
    
    return {
        "maximum": max(a, b, c),
        "minimum": min(a, b, c),
        "average": (a + b + c) / 3,
        "median": sorted_nums[1],
        "sum": a + b + c,
        "product": a * b * c,
        "range": max(a, b, c) - min(a, b, c),
        "sorted": sorted_nums
    }

# Enhanced version for any number of arguments
def math_operations_enhanced(*numbers: float) -> dict:
    \"\"\"Perform math operations on any number of arguments\"\"\"
    if not numbers:
        return {"error": "No numbers provided"}
    
    sorted_nums = sorted(numbers)
    n = len(numbers)
    
    return {
        "maximum": max(numbers),
        "minimum": min(numbers),
        "average": sum(numbers) / n,
        "median": sorted_nums[n//2] if n % 2 == 1 else (sorted_nums[n//2-1] + sorted_nums[n//2]) / 2,
        "sum": sum(numbers),
        "product": math.prod(numbers),
        "range": max(numbers) - min(numbers),
        "count": n,
        "sorted": sorted_nums
    }

# Example usage
if __name__ == "__main__":
    # Test cases
    test_numbers = [
        (1, 2, 3),
        (10, 5, 8),
        (-5, 0, 5),
        (2.5, 3.5, 1.5)
    ]
    
    print("Math Operations:")
    print("=" * 50)
    
    for a, b, c in test_numbers:
        print(f"Numbers: {a}, {b}, {c}")
        print(f"Max: {find_max(a, b, c)}")
        print(f"Min: {find_min(a, b, c)}")
        print(f"Average: {find_average(a, b, c):.2f}")
        
        # Comprehensive operations
        results = math_operations(a, b, c)
        print(f"All operations: {results}")
        print("-" * 30)
    
    # Test enhanced version
    print("\\nEnhanced version with multiple numbers:")
    enhanced_results = math_operations_enhanced(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(f"Operations on 1-10: {enhanced_results}")
```""",
                "explanation": "Mathematical operations including maximum, minimum, average, median, sum, product, and range calculations. Includes both basic three-number functions and enhanced version for any number of arguments with proper median calculation."
            },
            "email_validation": {
                "patterns": [
                    r"validate.*email", r"email.*regex", r"check.*email", r"regex.*email",
                    r"email.*validation", r"python.*email", r"verify.*email"
                ],
                "code": """```python
import re
from typing import Tuple, Dict, List

def validate_email(email: str) -> Tuple[bool, str]:
    \"\"\"
    Validate email address using comprehensive regex patterns
    
    Args:
        email: The email address to validate
    
    Returns:
        Tuple of (is_valid: bool, message: str)
    \"\"\"
    # Comprehensive email regex pattern (RFC 5322 compliant)
    rfc_pattern = r\"^[a-zA-Z00-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$\"
    
    # Simplified pattern for most common cases
    simple_pattern = r\"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$\"
    
    # Basic length checks
    if len(email) > 254:
        return False, \"Email too long (max 254 characters)\"
    
    if \"@\" not in email:
        return False, \"Email must contain @ symbol\"
    
    # Check local part length (before @)
    local_part = email.split(\"@\")[0]
    if len(local_part) > 64:
        return False, \"Local part too long (max 64 characters)\"
    
    # Regex validation
    if re.match(rfc_pattern, email):
        return True, \"Valid email (RFC 5322 compliant)\"
    elif re.match(simple_pattern, email):
        return True, \"Valid email (common format)\"
    else:
        return False, \"Invalid email format\"

def advanced_email_validation(email: str) -> Dict[str, any]:
    \"\"\"
    Advanced email validation with detailed analysis
    
    Returns:
        Dictionary with validation results and suggestions
    \"\"\"
    result = {
        \"email\": email,
        \"is_valid\": False,
        \"reasons\": [],
        \"suggestions\": []
    }
    
    # Basic checks
    if not email.strip():
        result[\"reasons\"].append(\"Email is empty\")
        return result
    
    # Length checks
    if len(email) > 254:
        result[\"reasons\"].append(\"Email exceeds maximum length of 254 characters\")
    
    # @ symbol check
    if \"@\" not in email:
        result[\"reasons\"].append(\"Missing @ symbol\")
        result[\"suggestions\"].append(\"Add @ symbol to the email address\")
    else:
        local_part, domain = email.split(\"@\", 1)
        
        # Local part validation
        if len(local_part) > 64:
            result[\"reasons\"].append(\"Local part (before @) too long\")
        
        if not local_part:
            result[\"reasons\"].append(\"Missing local part (before @)\")
        
        # Domain validation
        if not domain:
            result[\"reasons\"].append(\"Missing domain part (after @)\")
        elif \".\" not in domain:
            result[\"reasons\"].append(\"Domain missing dot separator\")
    
    # Regex validation
    is_valid, message = validate_email(email)
    if is_valid:
        result[\"is_valid\"] = True
    else:
        result[\"reasons\"].append(message)
    
    # Additional suggestions
    if \" \" in email:
        result[\"suggestions\"].append(\"Remove spaces from email address\")
    
    if email != email.lower():
        result[\"suggestions\"].append(\"Email addresses are case-insensitive; consider using lowercase\")
    
    return result

# Example usage and testing
if __name__ == \"__main__\":
    test_emails = [
        \"user@example.com\",
        \"invalid-email\",
        \"name@domain.co.uk\", 
        \"test@sub.domain.com\",
        \"missing@tld\",
        \"john.doe@company.org\",
        \"user@localhost\",  # Special case
        \"me@example.c\",    # Short TLD
        \"\"  # Empty email
    ]
    
    print(\"Email Validation Results:\")
    print(\"=\" * 50)
    
    for email in test_emails:
        # Basic validation
        is_valid, message = validate_email(email)
        status = \"✅ VALID\" if is_valid else \"❌ INVALID\"
        print(f\"{status}: {email}\")
        print(f\"   Message: {message}\")
        
        # Advanced validation for invalid emails
        if not is_valid:
            advanced = advanced_email_validation(email)
            if advanced[\"reasons\"]:
                print(f\"   Reasons: {', '.join(advanced['reasons'])}\")
            if advanced[\"suggestions\"]:
                print(f\"   Suggestions: {', '.join(advanced['suggestions'])}\")
        
        print(\"-\" * 30)
```""",
                "explanation": "Comprehensive email validation system with both basic and advanced checking. Includes RFC 5322 compliant regex patterns, length validation, domain checking, and detailed error reporting with suggestions. Handles edge cases and provides helpful feedback for invalid emails."
            },
            "web_scraping": {
                "patterns": [
                    r"scrape.*web", r"web.*scrap", r"beautifulsoup", r"requests.*html",
                    r"extract.*title", r"get.*webpage", r"parse.*html", r"scrap.*content",
                    r"title.*webpage", r"web.*content"
                ],
                "code": """```python
import requests
from bs4 import BeautifulSoup
from typing import Dict, List, Optional

def scrape_titles(url: str) -> Dict[str, List[str]]:
    \"\"\"
    Scrape titles from a webpage using requests and BeautifulSoup
    
    Args:
        url: The URL of the webpage to scrape
    
    Returns:
        Dictionary containing various types of titles found on the page
    \"\"\"
    try:
        # Set headers to avoid being blocked
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive'
        }
        
        # Make the request with timeout
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        results = {
            'page_title': [],
            'h1_titles': [],
            'h2_titles': [],
            'h3_titles': [],
            'h4_titles': [],
            'h5_titles': [],
            'h6_titles': [],
            'meta_titles': []
        }
        
        # Page title
        if soup.title and soup.title.string:
            results['page_title'].append(soup.title.string.strip())
        
        # Heading tags (h1 to h6)
        for level in range(1, 7):
            headings = soup.find_all(f'h{level}')
            for heading in headings:
                if heading.text.strip():
                    results[f'h{level}_titles'].append(heading.text.strip())
        
        # Meta title tags
        meta_title = soup.find('meta', {'name': 'title'})
        if meta_title and meta_title.get('content'):
            results['meta_titles'].append(meta_title['content'].strip())
        
        # Open Graph title
        og_title = soup.find('meta', {'property': 'og:title'})
        if og_title and og_title.get('content'):
            results['meta_titles'].append(og_title['content'].strip())
        
        return results
        
    except requests.exceptions.RequestException as e:
        return {'error': f'Request failed: {str(e)}'}
    except Exception as e:
        return {'error': f'Scraping failed: {str(e)}'}

def scrape_with_retry(url: str, retries: int = 3) -> Optional[Dict]:
    \"\"\"Scrape with retry mechanism for reliability\"\"\"
    for attempt in range(retries):
        try:
            result = scrape_titles(url)
            if 'error' not in result:
                return result
            print(f"Attempt {attempt + 1} failed: {result['error']}")
        except Exception as e:
            print(f"Attempt {attempt + 1} failed with exception: {e}")
    
    return None

# Example usage and testing
if __name__ == \"__main__\":
    # Test URLs (replace with actual URLs you want to scrape)
    test_urls = [
        \"https://example.com\",
        \"https://httpbin.org/html\"  # Test page with HTML content
    ]
    
    print(\"Web Scraping Results:\")
    print(\"=\" * 50)
    
    for url in test_urls:
        print(f\"\\nScraping: {url}\")
        titles = scrape_titles(url)
        
        if 'error' in titles:
            print(f\"❌ Error: {titles['error']}\")
            # Try with retry mechanism
            retry_result = scrape_with_retry(url)
            if retry_result and 'error' not in retry_result:
                print(\"✅ Success on retry!\")
                titles = retry_result
            else:
                continue
        
        # Display results
        for title_type, title_list in titles.items():
            if title_list and title_type != 'error':
                print(f\"{title_type.upper()}:\")
                for i, title in enumerate(title_list, 1):
                    print(f\"  {i}. {title}\")
        
        print(\"-\" * 30)

# Additional utility functions
def save_titles_to_file(titles: Dict, filename: str) -> None:
    \"\"\"Save scraped titles to a text file\"\"\"
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for title_type, title_list in titles.items():
                if title_list and title_type != 'error':
                    f.write(f\"{title_type.upper()}:\\n\")
                    for title in title_list:
                        f.write(f\"  - {title}\\n\")
                    f.write(\"\\n\")
        print(f\"Titles saved to {filename}\")
    except Exception as e:
        print(f\"Error saving to file: {e}\")

# Usage example for file saving
# titles = scrape_titles(\"https://example.com\")
# save_titles_to_file(titles, \"scraped_titles.txt\")
```""",
                "explanation": "Comprehensive web scraping function using requests and BeautifulSoup to extract titles from webpages. Includes proper error handling, user-agent headers, timeout management, retry mechanism, and file saving functionality. Handles various types of titles including page title, heading tags (h1-h6), and meta titles."
            },
            "prime_numbers": {
                "patterns": [
                    r"prime.*number", r"check.*prime", r"is.*prime", r"prime.*function",
                    r"test.*prime", r"prime.*algorithm", r"number.*prime"
                ],
                "code": """```python
import math
from typing import List

def is_prime(n: int) -> bool:
    \"\"\"
    Check if a number is prime
    
    Args:
        n: Integer to check for primality
    
    Returns:
        True if prime, False otherwise
    
    Raises:
        ValueError: If n is less than 2
    \"\"\"
    if n < 2:
        raise ValueError(\"Prime numbers must be greater than or equal to 2\")
    
    # Quick checks for small numbers
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check divisibility up to sqrt(n)
    max_divisor = math.isqrt(n) + 1
    for i in range(3, max_divisor, 2):
        if n % i == 0:
            return False
    
    return True

def is_prime_optimized(n: int) -> bool:
    \"\"\"
    Optimized prime check with more quick checks
    
    Args:
        n: Integer to check for primality
    
    Returns:
        True if prime, False otherwise
    \"\"\"
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check divisibility by numbers of form 6k ± 1
    max_divisor = math.isqrt(n) + 1
    for i in range(5, max_divisor, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    
    return True

def generate_primes(limit: int) -> List[int]:
    \"\"\"
    Generate all prime numbers up to a limit using Sieve of Eratosthenes
    
    Args:
        limit: Upper bound for prime generation
    
    Returns:
        List of prime numbers
    \"\"\"
    if limit < 2:
        return []
    
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    
    for current in range(2, math.isqrt(limit) + 1):
        if sieve[current]:
            for multiple in range(current * current, limit + 1, current):
                sieve[multiple] = False
    
    return [num for num, is_prime in enumerate(sieve) if is_prime]

def prime_factors(n: int) -> List[int]:
    \"\"\"
    Find prime factors of a number
    
    Args:
        n: Number to factorize
    
    Returns:
        List of prime factors
    \"\"\"
    if n < 2:
        return []
    
    factors = []
    # Factor out 2s
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Factor out odd numbers
    f = 3
    while f * f <= n:
        if n % f == 0:
            factors.append(f)
            n //= f
        else:
            f += 2
    
    if n > 1:
        factors.append(n)
    
    return factors

# Example usage and testing
if __name__ == \"__main__\":
    print(\"Prime Number Functions:\")
    print(\"=\" * 40)
    
    # Test numbers
    test_numbers = [2, 3, 4, 17, 25, 29, 100, 101, 997]
    
    print(\"Basic prime check:\")
    for num in test_numbers:
        try:
            result = is_prime(num)
            print(f\"is_prime({num}) = {result}\")
        except ValueError as e:
            print(f\"is_prime({num}) = Error: {e}\")
    
    print(\"\\nOptimized prime check:\")
    for num in test_numbers:
        result = is_prime_optimized(num)
        print(f\"is_prime_optimized({num}) = {result}\")
    
    print(\"\\nPrime generation (primes up to 50):\")
    primes = generate_primes(50)
    print(primes)
    
    print(\"\\nPrime factorization:\")
    for num in [56, 100, 123, 997]:
        factors = prime_factors(num)
        print(f\"Prime factors of {num}: {factors}\")
    
    # Performance comparison
    print(\"\\nPerformance Note:\")
    print(\"• Basic check: O(√n) time complexity\")
    print(\"• Optimized check: ~O(√n/3) time complexity\") 
    print(\"• Sieve of Eratosthenes: O(n log log n) for generating primes\")
```""",
                "explanation": "Comprehensive prime number utilities including primality testing (basic and optimized versions), prime number generation using Sieve of Eratosthenes, and prime factorization. Includes proper error handling, mathematical optimizations, and performance analysis. Handles edge cases and provides educational examples."
            },
            "dictionary_operations": {
                "patterns": [
                    r"merge.*dict", r"dict.*merge", r"combine.*dict", r"update.*dict",
                    r"dictionary.*operation", r"python.*dict", r"join.*dict"
                ],
                "code": """```python
def merge_dicts(dict1: dict, dict2: dict) -> dict:
    \"\"\"Merge two dictionaries (dict2 values override dict1)\"\"\"
    return {**dict1, **dict2}

# Advanced merging with conflict resolution
def merge_dicts_advanced(dict1: dict, dict2: dict, 
                        conflict_strategy: str = 'override') -> dict:
    \"\"\"
    Merge dictionaries with configurable conflict handling
    
    Args:
        conflict_strategy: 'override', 'keep_first', or 'combine'
    \"\"\"
    result = dict1.copy()
    
    for key, value in dict2.items():
        if key in result:
            if conflict_strategy == 'override':
                result[key] = value
            elif conflict_strategy == 'keep_first':
                pass  # Keep original value
            elif conflict_strategy == 'combine':
                if isinstance(result[key], list) and isinstance(value, list):
                    result[key].extend(value)
                else:
                    result[key] = [result[key], value]
        else:
            result[key] = value
    
    return result

# Example usage
if __name__ == \"__main__\":
    dict_a = {'a': 1, 'b': 2, 'c': 3}
    dict_b = {'b': 20, 'd': 4, 'e': 5}
    
    print(\"Basic merge:\", merge_dicts(dict_a, dict_b))
    print(\"Override conflicts:\", merge_dicts_advanced(dict_a, dict_b, 'override'))
    print(\"Keep first:\", merge_dicts_advanced(dict_a, dict_b, 'keep_first'))
    print(\"Combine values:\", merge_dicts_advanced(dict_a, dict_b, 'combine'))
```""",
                "explanation": "Dictionary merging functions including basic merge and advanced version with conflict resolution strategies. Handles different data types and provides flexible merging options."
            },
            "file_writing": {
                "patterns": [
                    r"write.*file", r"list.*file", r"save.*file", r"output.*file",
                    r"write.*list", r"strings.*file", r"file.*write"
                ],
                "code": """```python
def write_list_to_file(filename: str, string_list: list, 
                      add_newlines: bool = True) -> bool:
    \"\"\"
    Write a list of strings to a file
    
    Args:
        filename: Name of the file to write
        string_list: List of strings to write
        add_newlines: Whether to add newline after each string
    
    Returns:
        True if successful, False otherwise
    \"\"\"
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for string in string_list:
                file.write(string)
                if add_newlines:
                    file.write('\\n')
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False

# Enhanced version with more options
def write_list_to_file_advanced(filename: str, data: list, 
                               mode: str = 'w', 
                               separator: str = '\\n',
                               encoding: str = 'utf-8') -> bool:
    \"\"\"
    Advanced file writing with customizable options
    \"\"\"
    try:
        with open(filename, mode, encoding=encoding) as file:
            for i, item in enumerate(data):
                file.write(str(item))
                if i < len(data) - 1:  # Don't add separator after last item
                    file.write(separator)
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False

# Example usage
if __name__ == \"__main__\":
    # Sample data
    lines = [\"First line\", \"Second line\", \"Third line\", \"Fourth line\"]
    
    # Basic writing
    success = write_list_to_file(\"output.txt\", lines)
    print(f\"Basic write successful: {success}\")
    
    # Advanced writing with custom separator
    data = [\"apple\", \"banana\", \"cherry\"]
    success = write_list_to_file_advanced(\"fruits.csv\", data, separator=\",\")
    print(f\"CSV write successful: {success}\")
    
    # Append mode
    more_data = [\"Fifth line\", \"Sixth line\"]
    success = write_list_to_file_advanced(\"output.txt\", more_data, mode=\"a\")
    print(f\"Append successful: {success}\")
```""",
                "explanation": "File writing functions for lists of strings. Includes basic newline-separated writing and advanced version with customizable separators, file modes, and encoding. Handles errors properly and provides flexible output options."
            }
        }
