{
    'variables': { 'target_arch%': 'x64' },

    'target_defaults': {
        'default_configuration': 'Debug',
        'configuration': {
            'Debug': {
                'defines': [ 'DEBUG', '_DEBUG' ],
                'msvs_settings': {
                    'VSSLCompilerTool': {
                        'RuntimeLibrary': 1, #static debug
                    },
                },
            },
            'Release': {
                'defines': [ 'NODEBUG' ],
                'msvs_settings': {
                    'VSSLCompilerTool': {
                        'RuntimeLibrary': 0, #static release
                    },
                },
            },
        },
        'msvs_settings': {
            'VCLinkerTool': {
                'GenerateDebugInformation': 'true',
            },
        },
    },

    'targets': [
        {
            'target_name': 'libspeexdsp',
            'type': 'static_library',
            'sources': [
                'speex-1.2.0/libspeex/bits.c',
                'speex-1.2.0/libspeex/cb_search.c',
                'speex-1.2.0/libspeex/exc_5_64_table.c',
                'speex-1.2.0/libspeex/exc_5_256_table.c',
                'speex-1.2.0/libspeex/exc_8_128_table.c',
                'speex-1.2.0/libspeex/exc_10_16_table.c',
                'speex-1.2.0/libspeex/exc_10_32_table.c',
                'speex-1.2.0/libspeex/exc_20_32_table.c',
                'speex-1.2.0/libspeex/filters.c',
                'speex-1.2.0/libspeex/gain_table.c',
                'speex-1.2.0/libspeex/gain_table_lbr.c',
                'speex-1.2.0/libspeex/hexc_10_32_table.c',
                'speex-1.2.0/libspeex/hexc_table.c',
                'speex-1.2.0/libspeex/high_lsp_tables.c',
                'speex-1.2.0/libspeex/kiss_fft.c',
                'speex-1.2.0/libspeex/kiss_fftr.c',
                'speex-1.2.0/libspeex/lpc.c',
                'speex-1.2.0/libspeex/lsp.c',
                'speex-1.2.0/libspeex/lsp_tables_nb.c',
                'speex-1.2.0/libspeex/ltp.c',
                'speex-1.2.0/libspeex/modes.c',
                'speex-1.2.0/libspeex/modes_wb.c',
                'speex-1.2.0/libspeex/nb_celp.c',
                'speex-1.2.0/libspeex/quant_lsp.c',
                'speex-1.2.0/libspeex/smallft.c',
                'speex-1.2.0/libspeex/speex.c',
                'speex-1.2.0/libspeex/speex_callbacks.c',
                'speex-1.2.0/libspeex/speex_header.c',
                'speex-1.2.0/libspeex/stereo.c',
                'speex-1.2.0/libspeex/vbr.c',
                'speex-1.2.0/libspeex/vq.c',
                'speex-1.2.0/libspeex/window.c'
            ],
            'cflags': [
                '-fvisibility=hidden',
                '-W',
                '-Wstrict-prototypes',
                '-Wno-parentheses',
                '-Wno-unused-parameter',
                '-Wno-sign-compare',
                '-Wno-unused-variable',
            ],
            'include_dirs': [
                'config/speex-1.2.0/<(OS)/<(target_arch)',
                'speex-1.2.0/include',
            ],
            'defines': [
                'PIC',
                'HAVE_CONFIG_H',
                '_USE_MATH_DEFINES',
            ]
        }
    ]
}