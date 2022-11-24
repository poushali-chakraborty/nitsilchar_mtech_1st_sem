# include < stdio .h >
# include < sys / types .h >
# include < unistd .h >
int main () {
pid_t pid , mypid , myppid ;
pid = getpid ();
printf (" Before fork : Process id is %d\n", pid );
pid = fork ();
if ( pid < 0) {
perror (" fork () failure \n");
return 1;
}
// Child process
if ( pid == 0) {
mypid = getpid ();
myppid = getppid ();
printf (" Child Process id is %d and PPID is %d\n", mypid , myppid );
for (int i =0; i <4; i ++){
printf (" Child loop %d\n",i );
sleep (1);
}
} else { // Parent process
for (int j =0; j <4; j ++){
printf (" Parent loop %d\n",j );
sleep (2);
}
mypid = getpid ();
myppid = getppid ();
printf (" Parent Process id is %d and PPID is %d\n", mypid , myppid );
printf (" Newly created process id or child pid is %d\n", pid );
}
return 0;
}