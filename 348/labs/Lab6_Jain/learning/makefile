# Makefile

# Compiler
CXX = g++

# Compiler flags
CXXFLAGS = -Wall -std=c++11 -fsanitize=address -fno-omit-frame-pointer 

# Target executable name
TARGET = main

# Object files
OBJS = q1p2.o matrix.o

# Build the target executable
$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)
	@rm -f $(OBJS)

# Compile source files to object files
q1p2.o: q1p2.cpp matrix.h
	$(CXX) $(CXXFLAGS) -c q1p2.cpp

matrix.o: matrix.cpp matrix.h
	$(CXX) $(CXXFLAGS) -c matrix.cpp

# Clean up the build
clean:
	rm -f $(OBJS) $(TARGET)
