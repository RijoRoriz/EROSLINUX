""" Python Character Mapping Codec generated from 'VENDORS/MICSFT/PC/CP865.TXT' with gencodec.py.

"""#"

import codecs

### Codec APIs

class Codec(codecs.Codec):

    def encode(self,input,errors='strict'):
        return codecs.charmap_encode(input,errors,encoding_map)

    def decode(self,input,errors='strict'):
        return codecs.charmap_decode(input,errors,decoding_table)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input,self.errors,encoding_map)[0]

class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_decode(input,self.errors,decoding_table)[0]

class StreamWriter(Codec,codecs.StreamWriter):
    pass

class StreamReader(Codec,codecs.StreamReader):
    pass

### encodings module API

def getregentry():
    return codecs.CodecInfo(
        name='cp865',
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    )

### Decoding Map

decoding_map = codecs.make_identity_dict(range(256))
decoding_map.update({
    0x0080: 0x00c7,     #  LATIN CAPITAL LETTER C WITH CEDILLA
    0x0081: 0x00fc,     #  LATIN SMALL LETTER U WITH DIAERESIS
    0x0082: 0x00e9,     #  LATIN SMALL LETTER E WITH ACUTE
    0x0083: 0x00e2,     #  LATIN SMALL LETTER A WITH CIRCUMFLEX
    0x0084: 0x00e4,     #  LATIN SMALL LETTER A WITH DIAERESIS
    0x0085: 0x00e0,     #  LATIN SMALL LETTER A WITH GRAVE
    0x0086: 0x00e5,     #  LATIN SMALL LETTER A WITH RING ABOVE
    0x0087: 0x00e7,     #  LATIN SMALL LETTER C WITH CEDILLA
    0x0088: 0x00ea,     #  LATIN SMALL LETTER E WITH CIRCUMFLEX
    0x0089: 0x00eb,     #  LATIN SMALL LETTER E WITH DIAERESIS
    0x008a: 0x00e8,     #  LATIN SMALL LETTER E WITH GRAVE
    0x008b: 0x00ef,     #  LATIN SMALL LETTER I WITH DIAERESIS
    0x008c: 0x00ee,     #  LATIN SMALL LETTER I WITH CIRCUMFLEX
    0x008d: 0x00ec,     #  LATIN SMALL LETTER I WITH GRAVE
    0x008e: 0x00c4,     #  LATIN CAPITAL LETTER A WITH DIAERESIS
    0x008f: 0x00c5,     #  LATIN CAPITAL LETTER A WITH RING ABOVE
    0x0090: 0x00c9,     #  LATIN CAPITAL LETTER E WITH ACUTE
    0x0091: 0x00e6,     #  LATIN SMALL LIGATURE AE
    0x0092: 0x00c6,     #  LATIN CAPITAL LIGATURE AE
    0x0093: 0x00f4,     #  LATIN SMALL LETTER O WITH CIRCUMFLEX
    0x0094: 0x00f6,     #  LATIN SMALL LETTER O WITH DIAERESIS
    0x0095: 0x00f2,     #  LATIN SMALL LETTER O WITH GRAVE
    0x0096: 0x00fb,     #  LATIN SMALL LETTER U WITH CIRCUMFLEX
    0x0097: 0x00f9,     #  LATIN SMALL LETTER U WITH GRAVE
    0x0098: 0x00ff,     #  LATIN SMALL LETTER Y WITH DIAERESIS
    0x0099: 0x00d6,     #  LATIN CAPITAL LETTER O WITH DIAERESIS
    0x009a: 0x00dc,     #  LATIN CAPITAL LETTER U WITH DIAERESIS
    0x009b: 0x00f8,     #  LATIN SMALL LETTER O WITH STROKE
    0x009c: 0x00a3,     #  POUND SIGN
    0x009d: 0x00d8,     #  LATIN CAPITAL LETTER O WITH STROKE
    0x009e: 0x20a7,     #  PESETA SIGN
    0x009f: 0x0192,     #  LATIN SMALL LETTER F WITH HOOK
    0x00a0: 0x00e1,     #  LATIN SMALL LETTER A WITH ACUTE
    0x00a1: 0x00ed,     #  LATIN SMALL LETTER I WITH ACUTE
    0x00a2: 0x00f3,     #  LATIN SMALL LETTER O WITH ACUTE
    0x00a3: 0x00fa,     #  LATIN SMALL LETTER U WITH ACUTE
    0x00a4: 0x00f1,     #  LATIN SMALL LETTER N WITH TILDE
    0x00a5: 0x00d1,     #  LATIN CAPITAL LETTER N WITH TILDE
    0x00a6: 0x00aa,     #  FEMININE ORDINAL INDICATOR
    0x00a7: 0x00ba,     #  MASCULINE ORDINAL INDICATOR
    0x00a8: 0x00bf,     #  INVERTED QUESTION MARK
    0x00a9: 0x2310,     #  REVERSED NOT SIGN
    0x00aa: 0x00ac,     #  NOT SIGN
    0x00ab: 0x00bd,     #  VULGAR FRACTION ONE HALF
    0x00ac: 0x00bc,     #  VULGAR FRACTION ONE QUARTER
    0x00ad: 0x00a1,     #  INVERTED EXCLAMATION MARK
    0x00ae: 0x00ab,     #  LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    0x00af: 0x00a4,     #  CURRENCY SIGN
    0x00b0: 0x2591,     #  LIGHT SHADE
    0x00b1: 0x2592,     #  MEDIUM SHADE
    0x00b2: 0x2593,     #  DARK SHADE
    0x00b3: 0x2502,     #  BOX DRAWINGS LIGHT VERTICAL
    0x00b4: 0x2524,     #  BOX DRAWINGS LIGHT VERTICAL AND LEFT
    0x00b5: 0x2561,     #  BOX DRAWINGS VERTICAL SINGLE AND LEFT DOUBLE
    0x00b6: 0x2562,     #  BOX DRAWINGS VERTICAL DOUBLE AND LEFT SINGLE
    0x00b7: 0x2556,     #  BOX DRAWINGS DOWN DOUBLE AND LEFT SINGLE
    0x00b8: 0x2555,     #  BOX DRAWINGS DOWN SINGLE AND LEFT DOUBLE
    0x00b9: 0x2563,     #  BOX DRAWINGS DOUBLE VERTICAL AND LEFT
    0x00ba: 0x2551,     #  BOX DRAWINGS DOUBLE VERTICAL
    0x00bb: 0x2557,     #  BOX DRAWINGS DOUBLE DOWN AND LEFT
    0x00bc: 0x255d,     #  BOX DRAWINGS DOUBLE UP AND LEFT
    0x00bd: 0x255c,     #  BOX DRAWINGS UP DOUBLE AND LEFT SINGLE
    0x00be: 0x255b,     #  BOX DRAWINGS UP SINGLE AND LEFT DOUBLE
    0x00bf: 0x2510,     #  BOX DRAWINGS LIGHT DOWN AND LEFT
    0x00c0: 0x2514,     #  BOX DRAWINGS LIGHT UP AND RIGHT
    0x00c1: 0x2534,     #  BOX DRAWINGS LIGHT UP AND HORIZONTAL
    0x00c2: 0x252c,     #  BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
    0x00c3: 0x251c,     #  BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    0x00c4: 0x2500,     #  BOX DRAWINGS LIGHT HORIZONTAL
    0x00c5: 0x253c,     #  BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    0x00c6: 0x255e,     #  BOX DRAWINGS VERTICAL SINGLE AND RIGHT DOUBLE
    0x00c7: 0x255f,     #  BOX DRAWINGS VERTICAL DOUBLE AND RIGHT SINGLE
    0x00c8: 0x255a,     #  BOX DRAWINGS DOUBLE UP AND RIGHT
    0x00c9: 0x2554,     #  BOX DRAWINGS DOUBLE DOWN AND RIGHT
    0x00ca: 0x2569,     #  BOX DRAWINGS DOUBLE UP AND HORIZONTAL
    0x00cb: 0x2566,     #  BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL
    0x00cc: 0x2560,     #  BOX DRAWINGS DOUBLE VERTICAL AND RIGHT
    0x00cd: 0x2550,     #  BOX DRAWINGS DOUBLE HORIZONTAL
    0x00ce: 0x256c,     #  BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL
    0x00cf: 0x2567,     #  BOX DRAWINGS UP SINGLE AND HORIZONTAL DOUBLE
    0x00d0: 0x2568,     #  BOX DRAWINGS UP DOUBLE AND HORIZONTAL SINGLE
    0x00d1: 0x2564,     #  BOX DRAWINGS DOWN SINGLE AND HORIZONTAL DOUBLE
    0x00d2: 0x2565,     #  BOX DRAWINGS DOWN DOUBLE AND HORIZONTAL SINGLE
    0x00d3: 0x2559,     #  BOX DRAWINGS UP DOUBLE AND RIGHT SINGLE
    0x00d4: 0x2558,     #  BOX DRAWINGS UP SINGLE AND RIGHT DOUBLE
    0x00d5: 0x2552,     #  BOX DRAWINGS DOWN SINGLE AND RIGHT DOUBLE
    0x00d6: 0x2553,     #  BOX DRAWINGS DOWN DOUBLE AND RIGHT SINGLE
    0x00d7: 0x256b,     #  BOX DRAWINGS VERTICAL DOUBLE AND HORIZONTAL SINGLE
    0x00d8: 0x256a,     #  BOX DRAWINGS VERTICAL SINGLE AND HORIZONTAL DOUBLE
    0x00d9: 0x2518,     #  BOX DRAWINGS LIGHT UP AND LEFT
    0x00da: 0x250c,     #  BOX DRAWINGS LIGHT DOWN AND RIGHT
    0x00db: 0x2588,     #  FULL BLOCK
    0x00dc: 0x2584,     #  LOWER HALF BLOCK
    0x00dd: 0x258c,     #  LEFT HALF BLOCK
    0x00de: 0x2590,     #  RIGHT HALF BLOCK
    0x00df: 0x2580,     #  UPPER HALF BLOCK
    0x00e0: 0x03b1,     #  GREEK SMALL LETTER ALPHA
    0x00e1: 0x00df,     #  LATIN SMALL LETTER SHARP S
    0x00e2: 0x0393,     #  GREEK CAPITAL LETTER GAMMA
    0x00e3: 0x03c0,     #  GREEK SMALL LETTER PI
    0x00e4: 0x03a3,     #  GREEK CAPITAL LETTER SIGMA
    0x00e5: 0x03c3,     #  GREEK SMALL LETTER SIGMA
    0x00e6: 0x00b5,     #  MICRO SIGN
    0x00e7: 0x03c4,     #  GREEK SMALL LETTER TAU
    0x00e8: 0x03a6,     #  GREEK CAPITAL LETTER PHI
    0x00e9: 0x0398,     #  GREEK CAPITAL LETTER THETA
    0x00ea: 0x03a9,     #  GREEK CAPITAL LETTER OMEGA
    0x00eb: 0x03b4,     #  GREEK SMALL LETTER DELTA
    0x00ec: 0x221e,     #  INFINITY
    9�B�kB�9�B�kB��B�kb��
�ioX�@��yoH�P��yoH�P��yoH�P��{oJ�R��s/B�Z��s.B�Z���GO
"q͕T��(�b��T��)�c����!�k����a�+����a�+���e�/��P��e�/��P��e�/�e3/����a3+����a�+���Dᳫ�\Dᳫ�\Dᳫ�\D�3��L��3��Lĝ�	�C��$���A��$���A��d���A��e���A��m��
�@��}�*@`i���*@`i��CQ��*8�BQ��*9�bQ��*�"Q��*Y�"S��(Y� C��8[� �Q�x{� �P�y{�� JR {��� Nr[��� nr$[��z �r�[�z(�z�S�z(�z�S�r(�z�S	�r)�{�R	ƈ����������������A�A�A�A�A�A�A�A�I�I�I�I�I�I�I�I�I�I�I�ImImImImI:�"���h�8� ���j�(�0���z�(�0���z�(�0���z�(�0���z� �8���r��޸�4���1�{����1�{���g5[��g�5�~�o�=�~��-�z�	�-�r��-W�3�����7������7*�x�Q�7+�y�P�7)�{��5)�{�R<�)�{�R���){KR��I���}��H���}��h���}��h���}��h���}��i����m��a����m��a����m���
d������
`����e͊p}�6eM��}.6eM��}.7eL��}/7eL��}/we��}o9�k�BM�;�i�@]�+�y�P]�+�y�P\�+�y�P^�*�x�Q~�,:�h�A~�,�����~U,�]|&��dE�M|6��dU�
q����
q������\G����\G����LG�����G�����C�����C�~�4��,��~�4��,ìT׻jL�7�TӻnL�7�TۻfL�7 T[��L87 V[��N85"FY��^:%"�Y)��:�b�)��z�g�T���c�D��{�s���k�3�H��+�3�H ��+�7�L��/�?�D��'����y秜4�Wh��6�Uh��6��SU(��6��RU)��6��PU+��6��pU��>ǃ0]K��~��0K������������������������������������������������������-�O,�-�M.�-�M.�G-�
��ci��*��I��%��ɘ&%��ɚ&'��ɚ&'�V7���g�V7���g���?mHD���?mHD���?"mhD���?"mhD���7"ehL���7 ejL���7(ebLՒ�7he"L�����Wc�����wc%�����wc%̘�ҷw#%̐�ڷ#-Ȁ�ʳo'=�����/7}�����/7}�!Yև�h�![օ�j�!S֍�b� S׍�b� S׍�b� Q���`1� Q���`1�Q���`0QL*���Ql&*���Al&:���Al&:���An$:���Cn$8���cn1$����n�$��ӹш�tE��7�Te��7�Te;�
7T�e;�
5V�g?�5V�g7s�֒�7r�ג���%,�~���%-��ʌ��%1w{ʌ��%1w{ʌ��%1w{ʬ��%w[ꬠ�W[j� ���["�q�#"�q�#*�1R�c*�1R�c*�3P�a.�3P�a�?3'P�a���3�P+a�0�{�)ǔ0�{�)ǔ0�{�)ǔ0�{�)ǔ0�{�)ǖ �	y�+מ �	q�#מ!�q�#���S���b��S���b��S���b��WS���b��WS���b��SS���b�nCӴ
�@����
�@����
�@��T��
�@���𴺝	M�ж��?m�ж��?m�Ѷ��>l�Ѷ��>l�Ѷ��>l�Ѷ��>ld�6�>�lW-�5��W,�4��W,�4��W,�4��W,�4��W-�5��W=�%��V=�%�)}���	y�8�ϮIY�"x���IY�"x���KY�"z���KY�"z����Q*��
HXq���HPy���HPy����h�"��m��h�"��lƻ�T ���Ļ�T���̻�T
���̺�U
���̲�]
���β�]���](��Ѯ��]h��Ѡ"�h��O��"�h��M��"�h��M�""phY�͟""phY�͟#qHX�̿#BqX���cB1����]�>S��]�>W��]�>G�S]K>�S]K>�W]O>�G]_>�G]_>�Q4�f�O*�S�F�o(�[�F�o ��OFo���ODm���6OdM���vO$
��#H�
��'H���'H���'I����K50���[}	7 ����u�?��4��u�?��5��u�?��7��w�=��7���5��7���5��6�4��ؑT��4��ܑP���r�@ ���r�  ���z� (���j�	8�,�ꎉ��-�뎈��hȇup��hʇwp��(��w0�K�(��w0�K�(��w0�K�(��v0�K�(��V0�K�(��V0�K�7����z��'����{��'��ׂ[�~'O�W�۳~/O�W�ۻ/N�V�ڻ/N�V�ڻ?/��������Tђ���Vѐ�ʃ��^ј�ʃ��^ј�ʋ��^٘�Λ��Zɜ���޸R����۞��ԑ��$_���� [����0K����p���p���p?ж'�ax�P���ax�P������B�����B� ����R� ����R� ����R�����P��
���@��
���@�7l/�>e&7L//�eL/�E�L�/��H�+��H�+��H�+�H+�E]��&'�uY��"�Uyh+"����h�"����`�*����`�*����`�*���k`9*���#�;���q����QC�[�דGC�[���GG�_���Fg����5V'�?��uV'�?��u�L�/��l�>�&�l�>�&�m�?�'�m�?�'�M�.��
i� >�J)���5�Vg��5�Vg��5�V0g��4�W0f���0�S0b���0�S0b���0�S0b���0�Spb����g�����e����ɢE�`Q�I�œ`Q�I�ő`Q�I�ŁpA�Y�ՁpA�Y�Ձ�3=+^�oa�9Z�kA�9Z�kA�ڇ�A�	څ�C{�	ޅ�Ck�	΅�Ck�	΅�C��$_����%'^��?ڹ-gV����mg����me��}��ie��}��ie��}��ie��}�*OQ��W2�:NA��V"�zn��vb0z���b0~���f1^�% ��F!����ơ���g�[Of���[Of���KOf����KNg����KFo����IfO����Y�϶[�Y�϶[���ȒD�����ʲF�����²N����т��ț�ӂ��ș��
�̹����*�������j�����`�*���d�.�Ƀ�&tt>]���&4t~]���"4p~Y���"5pY���"=pwY �)"�p�Y�6���]�6���]躶�AMh���@Mi���@Mi���PLy���P\y+��P�y�IXx�`���Y\h�p���Y\h�p���Y\h�p���Q\`�x���Q\`�x���Q\`�x���P\a�y��b90s֍�b90s֍�r� �	V�r� �	W�r� �	W�r� �	G�z�(��U�訢�U�˓$.��˓$.��˓$.ӟh�$�ӟh�&�ѝj�6���z�6��
[#���ZK!ZA!���Z@
!���ZB!���Zb(!���Z"h!͵�Z#i!̵���g�q5���g�a5���G�$!灴G�$ 恼G�$(C� (�<S$0�n�=S%0�oz8� ߬�jz8� ߬�jz����,��:����,��:����.��:����.��:����.�躺|�..��U��Y���u��Y���u��y�3��t��y�3��v��y�3��V��x�2��V��X��eVL�ء��Ă�ȿm+?Ƃ�Ƚm)?悴ȝm	?�����mI?�����mI?�����mM?�����m]?�ȉm?�F�%U��f�Q4�,�&�EQt�lE&]E�tlE"]A�phA"YA�phQ"IA�ph�"�AEp�hz߇�ͤh{އ�ͥhk·�͵h+�����h+�����`*;�����@"{��ե� "z��դ�i�@f�4�k�BF��=c�JF��=���F^=���D^?���d_6�A��O���A���E��i5���X�y7���H�9�ɵ&*9��I��*9��I��*9��I��
y��i��H
x��i�I���������}����O�,m��N�-m��L�/m��L�/i�����a����̭�!�熆D����#Єd����!�d������dբ��A��lժ��A��lԪ��@����*�I`x���*�I`x	m�?['	m�?['	����[�I�Q�ݿ�I�Q�ݷ�K�S�߷�K�S�߷�K�S�߷��̺�6����ܻ�7��ܻ�7��ܻ�7��ܻ�7��ܿ�3����ܟ��Ֆ�ݟ��՗2���x�42���x�4:Ѷ�p�t:ж�p�u:Զ�p�q;Է�q�qԗ�Q�2q՗�Q�2p蟺Փp"韻Ւp"韻Ւp"韻Ւp"靻גr 靻גr ���ׂr ���ւs!�z�����z�����z����0��z���p��~���p��n���t����(�KtzQ�`(xK�zga�5+-HcA �1)hc� M1�)�c� L1�)�c� N1�)�a�n3�+�i�
n;�#���n���˭
�̄���
�̅�	��J�����$J�
A�:1�c�JA �r�[h� �r�[l� �r�[lϗ rI[�ϗ rI[�ϕ rK[�ϝ`	2C�`�2�f�8��	/��Ɛ)-�X놐i-�X놐i-�P뎐a-�@ꞑq,�@➙q$�U@���qd�z���b�{� 2��c�{] ��Ec>{] ��Ec>{_ ��Gc<{_ ��Gc<k_��Gs<k^��Fs=@�qLi/�B�slk�>B*s�k��*3�+���"3�+���"2�*���"2�*���"2�*���/p��7L�-`��5N�= ҝ%C^�=!Ҝ%B^�=)Ҕ%J^�<9ӄ$Z_�<9ӄ$Z_�|9��dZ��|}M�U��|mM�U��lm]�Eȏ��mݫ�ȏ��oݩ�ʋ��o٩�ʃ��oѩ���`oQ�I���Y�����Y����S�����R�����Z�����Z������P���q#P
������5�V{g���%�Fwڣ�e�7Z�kes�7Z�kes�7[�jur�'S�b5zV�g���5�Vvg٪U����ݪQ����ͪA����M����dM����dL����eD����mKD����mK��+����+�����k���Z��j���[��n���_��
n���_�
.����
/���Ǵ��(	z�Ǵ��(	z�Ǥ��(z�Ǥ��(z�Ǥ��(z�祭�Z����H����H�KX0���K\0���TYp���TYp���T]t���U]t���u]?t���u\?u�᪤�S]z���S\z���SLz���SLz���WL~���WL~��E&l>�2E��>�Nc�g���ng_�G���nG_�G���oG^�F���mG\�D���}EL�T����U̓��X��U͓��Y�S��JK�0�C��H[� �C��@[� �C��@[� �A��@Y�"�A��DY�"�AٮdY�"�@ٯdX�#�ܦ3���ݦ2���ͦ"���ͦ"���ͦ"���ͦ"�����*[݅��E�[]���j�&���J�1$���
�q4���E
�qt���E�st���E�ct��oe���T^Xo�;��^I�ئL�I�Ȧ\�i�#Ȇ\����\T���\T���LP���L@����RL �upD�\��uPD�\��}L�T��}L�T��}L�T��N�V�<�_n�v�<�_n�v����b������c�������c������c������c�������c������k������k������y9�� �{9���s9P��H�39P�� H�31Q�� I�2qݞ`i�Qqݞ`i�Q
��i��
���������2222�2�2�2�2�:�:�:�:���������������������Tp���Ae�tp���AE�4PÎ�a�4PÎ�a�4PÎ�a�4QÏ�`�4qï�@�5q¯�@nnnnl=l=l=l=l=l=l=l=�=�=�=�=�9�9�9�9�9�9�9�9̹̹̹̹��������jyr�+83kys�+93{9cZ�k)s{8c[�j)r{:cY�h)pyay�H+PYAy�HP��yMH�P�@��p̟�D��pȟ�SL�0�ߣRL�1�ޣZL�9�֣JL��)�Ƴ�\w���F3��w+�PFV�-��N�W�,��O�G�<��_�G�<��_�G�<��_�C�8��[�S�(��K����˓�e�����a����9�i-�5̹�)-�5���))�1���+)�1���+)�1��'�)m1���ʦo2=x��Φk29x��&c�1���'c�1���/c�1��/a�3�̯i;;q��̮i:;pa�����e�񳻚ua�3���aa3+���ca1+���Ce/8���Cm'8���Cm'8��������������--------))))))))iiii(d��0K�,d��4O�$d��<G�dd��|�dl��|�el��}�m�Qu�`��Q���`ޔ)JR��R߄(ZS��B߄(ZS��B_��ZӵnB_��Xӷn@_��HӧnPO��Hç~PO��Hç~Pt�&�`�2v�$�
1� X;�
��r?C�[�1�R;c�{����+�������+�������+�������)��ߝ���	���ݕ��IǏߒ�}Y���h��|I���x��\I���x��\I���x��\A���p��XQ���`��PQ���`��PP���aM]d��m\D�Ы�6�|��P�6�|��Q�6�|��S�7�}��s�9?�u��s�9�5�s�9(z��K��K(Z��K֤kZ��kքkHZ��+��kHR��+��cIB��*��sA��5"N��¼5bN������lݪ�����n������n������n������n������j������b����Ʈ�"��d�6�e�t�&�d����d���d���d���e���ЏuN�ڦ��5���>zɤ����>xɦ��Q�XI�2Qe��I2Ue��M6ud��m5d��-V5d��-V�,�,�,�,�<�<�<�<�|�|�|�|N|N|N|N|N|N|N|N|J|J|J|J|Z|Z|Z|Z|Z}Z}Z}Z}&<>_�ntv$<�NvV,4�N~Vlt�N>Vltw�F>^muw�F?^eT}7�7%T=7�w�*�*�*�*�:�:�:�:���������������������������������ӦӦӦ��������ӌ8��J �[���N �{���N �{���N�z���N�z���L�z���\�z���\ �{�1�RLc�{��rHC�[�Q�2h��Q�2h��Y�:h��Y�:h����h���|�d��.���>Ntgѽ�JTc�8jTC�8jUC�8jWC�:hWA��]Ha���Z]!��,�f��?��,�f��=��l�&��5�Zl&!���Zd.!���^d.%���~�,��Y>�l�E�Y���������������������������������������������������_ݙ�����_ݙ���������٥��ѥ�훎�ѧ�����Q�2����Q�2��to&%���vo$%
eX�@���
eP�H���e@�X���e ����R� #@�qR߂��D�߂��D���!��9���!��9���!��9���#��;�ݚ��\�]���l\����`�B2��`�@2���`�H2m�\`D�2m�\dD�6o�^DF'�g�VDN'���D�'B�i2�`�I�i6�d�M��6}d7M��}�7͒��y�3͖��i�#̆2��i�#�r��i�#�����>�]Hl����}JL����}jL�ؾ�}*L�ھ�*N�ڿ�+N�ڷ�#N�7/�N��w�=��	�s�9��I��S���I��S���A��S���a��Q�����DQ?���EQ>۱~%,o�ّ|.O��\��'j�\��'k�\��'c�^��%s�H~�,�3�H>�l�E3�OI�2~���_I�2n����A:���A :���A :���C 8���K 0���K 0�_��t<Ӳ]��t>ѲU��6��2�h���Y2�h���Y:�+jܴ�[�+Jܔ�{�*Jݔ�{�ьt&R���d6R���$vR_���$vR_���$vR_���4fVO�јt&F�Иu'F$�$�$�$�%�%�%�%�%"%"%"%"%#%#%#%#%+%+%+%+%%%%KKKKKKKK�Kv���Gz�Kr���Cz��R<�Gc�o��<G��o��8C��k��(S��{��(S��;߆(XS��tla�P&Hvnq�@$X~fq�@,X��qj@�X��sjB�Z�0�Skb�z����c������c��
���;c̽
���;s̭���3sĭB���ss��B���sw��@���qw��`�Q7��`�Q7�駞�X�;
���H�+���H�+��H�+N��L�/N��\�?J���οB����ξB�+E���ܛ/E���؛'E���ЛgEN�ڲ��gGN�ڰ��fgO�ې��fgO�ې��ffO�ۑ���L�MT�/�L�LT�/���\�o�
&9��E��')��D����^d%����^d%��hĶ�Y��iķ�X��I���xB��I���xB��I���x@��K���z`��[&�]j��>['�\j�?Ĺa-3g�ƙc
�X�@�̢
�xp`�"*:xp`�"*:xr`� *8xb`�0*(p�h��"�p�h��"�9�!ѭ�k�;�#ѯ�i�;�#ѯ�i�{�c���)�{�c���)��g���-�_�G���
oy��ҧ�o��m�'��o��m�'��m��i�#��m��y�3��-��y�3��-$n6ˢ�� j6Ϣ�� _jv�❨`_*v��ݨ`W*~��ݠdW.~��٠D>������>+�y����(�w���)�wϔ�{	������{I������I����H�����@�s���@	�r�`֏kx��`֏kx�� ��c8�C�!��c9�B�!��c9�B�!��b9�B�!��b9�B$!_��9<B�X���_�\���O�L��E�����iE;����iG;
�w�/T��7�/T��7A�͠�h4C�Ϡ	�j4S�ߠ�z4���Y�:4���Y�:<���[�8,���[�8,Q�ݸ�x,Z����sC^����wC~���4�WC��r״��C��rߴ��K��s����k��c����k��c����j1�J?��)�3�H��+�3�H��+�3�H��+�3�H��+�1�J
��)�!�ZJ�9�!�ZJ�9ƧnHӿ
/kT��s7+kP��s3kp��s�k��Ms��o�%����o�%����ﺥ� R����� GR�����GZ�����FZ�g�-�f��g�-��&���"SՍ�b��#Sԍ�b��S�bl�St�bl�[t�jnƁ{v�
~��;f�
��a�+����c�)����c�)����#�i����#�i����#�i���{3)y ܔ�z3(yܕ��X��(��2�x��)��2�x��!��3�y��!��1�{��!��1�{��!��q�;��)̆q�;��i̔��Eƃ�����Eă�������Ԡ�����Ԡ�����Ԣ�����բ���A�"���A�"$�v�_D�$�v�_d�64�f�O$�v4�f�O%�w4�f�O%�w4�f�O5�g$�v�_u�'�����uK'X����i\����mT@���qe�T@���qe�TD���ue�PD���ua�@���5q��7�L5����ѐ]�����Ӏ_�����ۀW�����ہW�����ۉW�����ٙU����z�u(�0azy�(30���u�['���U�6Y���ŶI����ŶI����ŶI����ŶI�̓�U�6i̓�U�6i���_2������O0������O8������N8������N8������N9����!��9�B�!��Y9�B�:8"[�jh�:9"Z�kh�:9"Z�kh�;9#Z�ki�?9'Z�km�8[�jM�_0GS�b
��x�iIJťxR�)IJͥpR�)AKݤ`S�(Q[ݴ`C�8Q[ܴaC�8P�~rÅ��R¥�=w��%^�=��J%�^�=��J%�^�=��K%�^���Rk��ޭ��Sk���_4�,���_5�-���$_�
�#�%H��3�%H��3L�eH��3L�eJ��1L�eJ��1D�m
�X�q�-
�X�q&z>�(t0'z?�(u0/z7�(}0/z7�(}0/~7�,}4+n3
�̠�,��*�젏,��*�졏-������T��{���t��{���t��{���u��{���w��zü��W��r������r�����(��b����B�!�H����a�I����`�K����b�[����r�[����r�Z����s��&�l����'�m����7�}��Q��7�}��Q��7�}��U��3�y��U��#�i��U��c�)��U�h�l:�"�H�+h���khZ�B�	�jh[�C�	�jh[�C��zlK�S��zlK�S��z,K�SK�z7bT�eO�~7fT�eO�~7fT�e�>7&T�e�>5&V�g�:5"V�gs2�*֦�Csr�j���k<Ψ��Gj<Ϩ��Gz��(�b��z��(�b��z�� �j��x��0�z��p��p�:��p��p�:���V���T�V���U�����9Ek�ָ��9k�ָ��9k�Ƹ��){�Ƙ��)%{J��1)�{'u\��m?%u^��m=5�N��-�5�N��-�5�N��-�1�J��)�9�BS��!�y�S��a��6]����Y'�?���VIg���EV�gl�ET�e}l�DT�e}m�dT�e.}M�dT�e.}M�aL��T��cL��T��c���#X����#X����"Y�� ��"Y�� ��"Y���ޚR�����ޞR��������Է�}�/�7�}�/�7�}�0/�7�u�p'�?����p����anananan`N`N`N`Npppp00000
0
0
0
2
2
2
2




gd�U-M}et�E/]u�m���'�����aŧ�����a�������c�������k�������k����D��]��E��]��E���W�E���W�E���S�D��9�sT-��T-���Tq���@e�Tp���Ae�Tx���IeET��&��eEP��&��aEp��&��AE0��&��0��f�������ȣ�����ȣ�����أҊ�����҂��Ș�҂��Ș�����H�+����I�*�+���a��;���q��;���q��:���p��8���r��8���r��8���r��8