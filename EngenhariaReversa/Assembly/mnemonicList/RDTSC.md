# RDTSC

Embora o x86 não tenha GPRs de 64 bits, ele pode combinar dois registradores, tipo( EDX:EAX ), e tratá-los como valores de 64 bits em alguns cenários; por exemplo usando a instrução RDTSC é possível gravar um valor de 64 bits em EDX:EAX

[https://docs.microsoft.com/pt-br/cpp/intrinsics/rdtsc?view=msvc-160](https://docs.microsoft.com/pt-br/cpp/intrinsics/rdtsc?view=msvc-160)