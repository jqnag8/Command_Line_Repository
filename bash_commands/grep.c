#include <stdio.h>
#include <stdlib.h>


char **create_lines(FILE *f) {
  // Make an array of lines (char *) from a file (f) 
  
  char **f_lines = malloc(sizeof(char *) * 10000);
  char *line = malloc(sizeof(char) * 1000);
  char c;
  int i = 0, j = 0;

  while ((c = fgetc(f)) != EOF) {
    if (c == '\n') {
      line[j] = '\0';
      f_lines[i] = line;
      i++;
      line = malloc(sizeof(char) * 1000);
      j = 0;
    } else {
      line[j] = c;
      j++;
    }
  }

  // For the las line if it does't end with '\n'
  if (j > 0) {
    line[j] = '\0';
    f_lines[i++] = line;
  }

  f_lines[i] = NULL; // End of array
  return f_lines;
}


void handmade_grep(char ** arr_lines, char target[]){
  // Similar behavior as grep. Search for a word in a file and return the line

  int resultado = 0;

  for (int i = 0; arr_lines[i] != NULL; i++) {
    char *linea = arr_lines[i];

    for (int j = 0; linea[j] != '\0'; j++)

      if (linea[j] == target[0]) {
        int index = j;

        while (linea[j] == target[j - index]){

          if (target[(j + 1) - index] == '\0') {
            resultado = 1;
            break;
          }

          j++;
          }
      }

    // If we found the line
    if (resultado){
      printf("%s\n", linea);
      break;
    }
  }

}


int main(int argc, char **args) {
  FILE *ptr_file = fopen(args[1], "r");
  if (! ptr_file) {
    printf("Error: Can't open the file.\n");
    return 1;
  }

  char **f_lines = create_lines(ptr_file);

  handmade_grep(f_lines, args[2]);

  // free every element from the array.
  for (int i = 0; f_lines[i] != NULL; i++) {
    free(f_lines[i]);
  }

  free(f_lines); 
  fclose(ptr_file);

  return 0;
}
