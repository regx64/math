// Flip-graph random walk for <3,3,3> over F2 (Kauers-Moosbauer style)
// 사용: ./flip333 <seed> <초> <재시작 한도>
// 27항 교과서식 분해에서 출발해 flip + reduce를 반복하고, rank 22 이하가 나오면 검증 후 found.txt에 저장한다.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>

#define MAXT 64
typedef uint16_t u16;
static u16 X[3][MAXT]; static int R;
static uint64_t s[2];
static inline uint64_t rnd(void){uint64_t s1=s[0];const uint64_t s0=s[1];s[0]=s0;s1^=s1<<23;s[1]=s1^s0^(s1>>17)^(s0>>26);return s[1]+s0;}

static u16 target[9][9];
static void init_target(void){memset(target,0,sizeof target);
 for(int i=0;i<3;i++)for(int j=0;j<3;j++)for(int k=0;k<3;k++) target[3*i+k][3*k+j]^=1<<(3*i+j);}
static int verify(void){u16 T[9][9];memset(T,0,sizeof T);
 for(int t=0;t<R;t++)for(int p=0;p<9;p++)if(X[0][t]>>p&1)for(int q=0;q<9;q++)if(X[1][t]>>q&1)T[p][q]^=X[2][t];
 return memcmp(T,target,sizeof T)==0;}
static void start27(void){R=0;for(int i=0;i<3;i++)for(int j=0;j<3;j++)for(int k=0;k<3;k++){X[0][R]=1<<(3*i+k);X[1][R]=1<<(3*k+j);X[2][R]=1<<(3*i+j);R++;}}
static void del(int t){R--;for(int p=0;p<3;p++)X[p][t]=X[p][R];}
static int reduce(void){int changed=1,any=0;
 while(changed){changed=0;
  for(int t=0;t<R;t++)if(!X[0][t]||!X[1][t]||!X[2][t]){del(t);changed=any=1;t--;}
  for(int i=0;i<R&&!changed;i++)for(int j=i+1;j<R&&!changed;j++)for(int p=0;p<3;p++){
    int q=(p+1)%3,r=(p+2)%3;
    if(X[q][i]==X[q][j]&&X[r][i]==X[r][j]){X[p][i]^=X[p][j];del(j);changed=any=1;break;}
  }}
 return any;}
static int ci[MAXT*MAXT*3],cj[MAXT*MAXT*3],cp[MAXT*MAXT*3];
static int flip(void){int n=0;
 for(int i=0;i<R;i++)for(int j=i+1;j<R;j++)for(int p=0;p<3;p++)if(X[p][i]==X[p][j]){ci[n]=i;cj[n]=j;cp[n]=p;n++;}
 if(!n)return 0; int c=rnd()%n,i=ci[c],j=cj[c],p=cp[c];
 if(rnd()&1){int t=i;i=j;j=t;}
 int q=(p+1)%3,r=(p+2)%3; if(rnd()&1){int t=q;q=r;r=t;}
 X[q][i]^=X[q][j]; X[r][j]^=X[r][i]; return 1;}
static void dump(const char*fn){FILE*f=fopen(fn,"w");for(int t=0;t<R;t++)fprintf(f,"%03x %03x %03x\n",X[0][t],X[1][t],X[2][t]);fclose(f);}

int main(int argc,char**argv){
 uint64_t seed=argc>1?strtoull(argv[1],0,10):time(0); double secs=argc>2?atof(argv[2]):60; long limit=argc>3?atol(argv[3]):2000000;
 s[0]=seed*0x9E3779B97F4A7C15ULL+1; s[1]=seed^0xDEADBEEF12345ULL; for(int i=0;i<10;i++)rnd();
 init_target(); start27(); if(!verify()){puts("bad start");return 1;}
 long hist[30]={0}; long steps=0,since=0,restarts=0; int best=99; clock_t st=clock();
 while((double)(clock()-st)/CLOCKS_PER_SEC<secs){
  if(!flip()){start27();restarts++;continue;}
  steps++;since++;
  if(reduce()){since=0; if(R<best){best=R;} hist[R]++;
    if(R<=22){ if(verify()){printf("FOUND rank %d seed %lu\n",R,seed);dump("found.txt");return 0;} else {puts("verify fail");return 1;} }
    if(R==23){ static int dumped=0; if(!dumped&&verify()){dump("r23.txt");dumped=1;} }
  }
  if(since>(R==23?limit*40:limit)){start27();restarts++;since=0;}
 }
 printf("seed %lu steps %ld restarts %ld best %d | reached23 %ld reached24 %ld reached25 %ld\n",seed,steps,restarts,best,hist[23],hist[24],hist[25]);
 return 0;}
