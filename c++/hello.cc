#include <node.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#ifdef __cplusplus
extern "C"
{
#endif
#include <speex/speex.h>
#include <speex/speex_callbacks.h>
#ifdef __cplusplus
}
#endif

#ifdef FIXED_DEBUG
extern long long spx_mips;
#endif

#define FRAME_SIZE 160
#ifdef FIXED_DEBUG
extern long long spx_mips;
#endif

#define FRAME_SIZE 160
using namespace v8;

void Add(const FunctionCallbackInfo<Value>& args) {
    Isolate* isolate = Isolate::GetCurrent();
    HandleScope scope(isolate);
    void *st;
    FILE *fin,*fout;
    short in[FRAME_SIZE];
    float input[FRAME_SIZE];
    char cbits[200];
    int nbBytes;

    SpeexBits bits;
    int i,tmp;

    st = speex_encoder_init(&speex_nb_mode);

    tmp = 8;
    speex_encoder_ctl(st,SPEEX_SET_QUALITY,&tmp);

    Local<Value> in_addr = args[0];
    Local<String> ss = in_addr->ToString();
    String::Utf8Value value(ss);
    char* c =  *value;
    fin = fopen(c,"r");

        Local<Value> out_addr = args[1];
        Local<String> out_addr_str = out_addr->ToString();
        String::Utf8Value value1(out_addr_str);
        char* o = *value1;
        fout = fopen(o,"w");


    speex_bits_init(&bits);
    while(1){
        fread(in,sizeof(short),FRAME_SIZE,fin);
        if(feof(fin))
            break;
        for(i = 0;i<FRAME_SIZE;i++){
            input[i] = in[i];
        }
        speex_bits_reset(&bits);
        speex_encode(st,input,&bits);
        nbBytes = speex_bits_write(&bits,cbits,200);
        fwrite(&nbBytes, sizeof(int), 1, stdout);
        fwrite(cbits, 1, nbBytes, stdout);
        fwrite(input,sizeof(short),FRAME_SIZE,fout);
    }


   speex_encoder_destroy(st);
   /*Destroy the bit-packing struct*/
   speex_bits_destroy(&bits);
   fclose(fin);

}

void Init(Handle<Object> exports) {
  NODE_SET_METHOD(exports, "add", Add);
}

NODE_MODULE(hello, Init)