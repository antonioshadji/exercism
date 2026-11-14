#include "rna_transcription.h"
#include <string.h>


char *to_rna(const char *dna)
{
    for (int i = 0; i < strlen(dna); i++){
        if (strcmp(dna, "C") == 0) return 'G';
    }
}
