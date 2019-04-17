{
  "targets": [
    {
      "target_name": "hello",
      "sources": ["./c++/hello.cc", ],
      "dependencies":[
        "deps/binding.gyp:libspeexdsp"
      ],
        'cflags': [
                      '-pthread',
                      '-fno-exceptions',
                      '-fno-strict-aliasing',
                      '-Wall',
                      '-Wno-unused-parameter',
                      '-Wno-missing-field-initializers',
                      '-Wextra',
                      '-pipe',
                      '-fno-ident',
                      '-fdata-sections',
                      '-ffunction-sections',
                      '-fPIC'
                  ],
                  'defines': [
                      'LARGEFILE_SOURCE',
                      '_FILE_OFFSET_BITS=64',
                      'WEBRTC_TARGET_PC',
                      'WEBRTC_LINUX',
                      'WEBRTC_THREAD_RR',
                      'EXPAT_RELATIVE_PATH',
                      'GTEST_RELATIVE_PATH',
                      'JSONCPP_RELATIVE_PATH',
                      'WEBRTC_RELATIVE_PATH',
                      'POSIX',
                      '__STDC_FORMAT_MACROS',
                      'DYNAMIC_ANNOTATIONS_ENABLED=0'
                  ],
                        'include_dirs': [
                            'deps/speex-1.2.0/include',
                            'deps/config/speex-1.2.0/<(OS)/<(target_arch)',
                        ],
              }
  ]
}