Overview - Hoare logic
- Previously we have look at program specifications that involve pre and post conditions and  *manually* reason that the program implementation is correct (adheres to) with respect to the specification.
- As we also have experienced, such manual reasoning is difficult, time consuming, and error-prone, even for short "toy" examples shown class.
- Automatic testing is popular and widely-used, however not adequate for many domains and situations such as avionic systems and medical systems 
- Automatic verification is what required, and has enjoyed many successes in the real-world. For examples,
  - Hardware (e.g., circuit designs, CPU) are rigorous verified by chip makers
  - Companies and government organizations develop and rely on verification tools (e.g., Mars Rover, Avionic system of Airbus, Facebook newsfeeds and instagrams, Microsoft drivers are all verified in some ways). 

- Today we will learn about Hoare Logic, one of the most popular ways to *automatically* verify program correctness.
- Hoare logic:
  - a formal systems with a set of rules to formally reason about the correctness of a program with respect to given specifications
  - invited by Sir. Tony Hoare, who is the Turing award winner in 1980 , and in addition to Hoare logic, has developed many well-known concepts such as the *quicksort* algorithm and "null pointer" (the billion dollar mistake) 
  - standard for many practical verification techniques and tools
  

  
For this topic, you will learn about
- Hoare tripple: which describes how the program changes its states during execution
- Total vs. Partial correctness: Total correctness reasons both about program termination (e.g., the loop will eventually terminate) and that the program is correct and satisfies the postcondition when it terminates; whereas parial correctness *assumes* the program terminates and only deals with program correctness.
- Computing Weakenst Preconditions using Hoare rules: a set of rules for each types of statements in a program that leads to the weakest preconditions required for verification
- Finding and using Loop invariants: the crucial piece of information that the user needs to provide to enable verification automation under Hoare logic
- Formulating specifications, weakest preconditions, loop invariants as logical formulae
- Using SAT solver to automatically prove program correctness

