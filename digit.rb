class Num
    # Hash mapping method names (symbols) to digit strings
    DIGIT_MAP = {
      zero: '0', one: '1', two: '2', three: '3', four: '4',
      five: '5', six: '6', seven: '7', eight: '8', nine: '9'
    }.freeze # Freeze the hash as it shouldn't change
  
    # Initialize an instance with the first digit's string representation
    def initialize(digit_str)
      @number_string = digit_str
    end
  
    # Define CLASS methods (e.g., Num.one, Num.two)
    # These start the chain by creating a new Num instance.
    DIGIT_MAP.each do |method_name, digit|
      define_singleton_method(method_name) do
        # Create a new instance initialized with this digit's string
        new(digit)
      end
    end
  
    # Define INSTANCE methods (e.g., num_instance.one, num_instance.two)
    # These continue the chain by appending to the existing string.
    DIGIT_MAP.each do |method_name, digit|
      define_method(method_name) do
        # Append the new digit to the internal string
        @number_string += digit
        # Return self to allow further chaining
        self
      end
    end
  
    # Convert the stored number string to an integer
    def to_i
      @number_string.to_i
    end
  
  end