import pytest
from main import HashingFunctions

class Tests:
    def __init__(self, entropy):
        self.entropy = entropy
        self.phrase = None
        self.key = None
        self.hashes = HashingFunctions()

    def ent_to_phrase(self, word_list): #tests to see if provided entropy produces desired word list
        self.hashes.get_input(self.entropy)
        self.hashes.create_check_sum()
        self.hashes.create_word_list()
        self.phrase = ''.join(self.hashes.result_word_list)
        assert self.phrase == word_list

    def phrase_to_key(self, seed_as_hex): #tests to see if word list converts to desired master key
        self.hashes.create_binary_seed()
        self.key = self.hashes.binary_seed
        assert self.key == seed_as_hex


test1 = Tests("00000000000000000000000000000000")
test2 = Tests("7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f")
test3 = Tests("80808080808080808080808080808080")
test4 = Tests("ffffffffffffffffffffffffffffffff")
test5 = Tests("000000000000000000000000000000000000000000000000")
test6 = Tests("7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f")
test7 = Tests("808080808080808080808080808080808080808080808080")
test8 = Tests("ffffffffffffffffffffffffffffffffffffffffffffffff")
test9 = Tests("0000000000000000000000000000000000000000000000000000000000000000")
test10 = Tests("7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f")
test11 = Tests("8080808080808080808080808080808080808080808080808080808080808080")
test12 = Tests("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff")
test13 = Tests("9e885d952ad362caeb4efe34a8e91bd2")
test14 = Tests("6610b25967cdcca9d59875f5cb50b0ea75433311869e930b")
test15 = Tests("68a79eaca2324873eacc50cb9c6eca8cc68ea5d936f98787c60c7ebc74e6ce7c")
test16 = Tests("c0ba5a8e914111210f2bd131f3d5e08d")
test17 = Tests("6d9be1ee6ebd27a258115aad99b7317b9c8d28b6d76431c3")
test18 = Tests("9f6a2878b2520799a44ef18bc7df394e7061a224d2c33cd015b157d746869863")
test19 = Tests("23db8160a31d3e0dca3688ed941adbf3")
test20 = Tests("8197a4a47f0425faeaa69deebc05ca29c0a5b5cc76ceacc0")
test21 = Tests("066dca1a2bb7e8a1db2832148ce9933eea0f3ac9548d793112d9a95c9407efad")
test22 = Tests("f30f8c1da665478f49b001d94c5fc452")
test23 = Tests("c10ec20dc3cd9f652c7fac2f1230f7a3c828389a14392f05")
test24 = Tests("f585c11aec520db57dd353c69554b21a89b20fb0650966fa0a9d6f74fd989d8f")


test1.ent_to_phrase("abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about")
test2.ent_to_phrase("legal winner thank year wave sausage worth useful legal winner thank yellow")
test3.ent_to_phrase("letter advice cage absurd amount doctor acoustic avoid letter advice cage above")
test4.ent_to_phrase("zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo wrong")
test5.ent_to_phrase("abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon agent")
test6.ent_to_phrase("legal winner thank year wave sausage worth useful legal winner thank year wave sausage worth useful legal will")
test7.ent_to_phrase("letter advice cage absurd amount doctor acoustic avoid letter advice cage absurd amount doctor acoustic avoid letter always")
test8.ent_to_phrase("zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo when")
test9.ent_to_phrase("abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon art")
test10.ent_to_phrase("legal winner thank year wave sausage worth useful legal winner thank year wave sausage worth useful legal winner thank year wave sausage worth title")
test11.ent_to_phrase("letter advice cage absurd amount doctor acoustic avoid letter advice cage absurd amount doctor acoustic avoid letter advice cage absurd amount doctor acoustic bless")
test12.ent_to_phrase("zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo zoo vote")
test13.ent_to_phrase("ozone drill grab fiber curtain grace pudding thank cruise elder eight picnic")
test14.ent_to_phrase("gravity machine north sort system female filter attitude volume fold club stay feature office ecology stable narrow fog")
test15.ent_to_phrase("hamster diagram private dutch cause delay private meat slide toddler razor book happy fancy gospel tennis maple dilemma loan word shrug inflict delay length")
test16.ent_to_phrase("scheme spot photo card baby mountain device kick cradle pact join borrow")
test17.ent_to_phrase("horn tenant knee talent sponsor spell gate clip pulse soap slush warm silver nephew swap uncle crack brave")
test18.ent_to_phrase("panda eyebrow bullet gorilla call smoke muffin taste mesh discover soft ostrich alcohol speed nation flash devote level hobby quick inner drive ghost inside")
test19.ent_to_phrase("cat swing flag economy stadium alone churn speed unique patch report train")
test20.ent_to_phrase("light rule cinnamon wrap drastic word pride squirrel upgrade then income fatal apart sustain crack supply proud access")
test21.ent_to_phrase("all hour make first leader extend hole alien behind guard gospel lava path output census museum junior mass reopen famous sing advance salt reform")
test22.ent_to_phrase("vessel ladder alter error federal sibling chat ability sun glass valve picture")
test23.ent_to_phrase("scissors invite lock maple supreme raw rapid void congress muscle digital elegant little brisk hair mango congress clump")
test24.ent_to_phrase("void come effort suffer camp survey warrior heavy shoot primary clutch crush open amazing screen patrol group space point ten exist slush involve unfold")

test1.phrase_to_key("c55257c360c07c72029aebc1b53c05ed0362ada38ead3e3e9efa3708e53495531f09a6987599d18264c1e1c92f2cf141630c7a3c4ab7c81b2f001698e7463b04")
test2.phrase_to_key("2e8905819b8723fe2c1d161860e5ee1830318dbf49a83bd451cfb8440c28bd6fa457fe1296106559a3c80937a1c1069be3a3a5bd381ee6260e8d9739fce1f607")
test3.phrase_to_key("d71de856f81a8acc65e6fc851a38d4d7ec216fd0796d0a6827a3ad6ed5511a30fa280f12eb2e47ed2ac03b5c462a0358d18d69fe4f985ec81778c1b370b652a8")
test4.phrase_to_key("ac27495480225222079d7be181583751e86f571027b0497b5b5d11218e0a8a13332572917f0f8e5a589620c6f15b11c61dee327651a14c34e18231052e48c069")
test5.phrase_to_key("035895f2f481b1b0f01fcf8c289c794660b289981a78f8106447707fdd9666ca06da5a9a565181599b79f53b844d8a71dd9f439c52a3d7b3e8a79c906ac845fa")
test6.phrase_to_key("f2b94508732bcbacbcc020faefecfc89feafa6649a5491b8c952cede496c214a0c7b3c392d168748f2d4a612bada0753b52a1c7ac53c1e93abd5c6320b9e95dd")
test7.phrase_to_key("107d7c02a5aa6f38c58083ff74f04c607c2d2c0ecc55501dadd72d025b751bc27fe913ffb796f841c49b1d33b610cf0e91d3aa239027f5e99fe4ce9e5088cd65")
test8.phrase_to_key("0cd6e5d827bb62eb8fc1e262254223817fd068a74b5b449cc2f667c3f1f985a76379b43348d952e2265b4cd129090758b3e3c2c49103b5051aac2eaeb890a528")
test9.phrase_to_key("bda85446c68413707090a52022edd26a1c9462295029f2e60cd7c4f2bbd3097170af7a4d73245cafa9c3cca8d561a7c3de6f5d4a10be8ed2a5e608d68f92fcc8")
test10.phrase_to_key("bc09fca1804f7e69da93c2f2028eb238c227f2e9dda30cd63699232578480a4021b146ad717fbb7e451ce9eb835f43620bf5c514db0f8add49f5d121449d3e87")
test11.phrase_to_key("c0c519bd0e91a2ed54357d9d1ebef6f5af218a153624cf4f2da911a0ed8f7a09e2ef61af0aca007096df430022f7a2b6fb91661a9589097069720d015e4e982f")
test12.phrase_to_key("dd48c104698c30cfe2b6142103248622fb7bb0ff692eebb00089b32d22484e1613912f0a5b694407be899ffd31ed3992c456cdf60f5d4564b8ba3f05a69890ad")
test13.phrase_to_key("274ddc525802f7c828d8ef7ddbcdc5304e87ac3535913611fbbfa986d0c9e5476c91689f9c8a54fd55bd38606aa6a8595ad213d4c9c9f9aca3fb217069a41028")
test14.phrase_to_key("628c3827a8823298ee685db84f55caa34b5cc195a778e52d45f59bcf75aba68e4d7590e101dc414bc1bbd5737666fbbef35d1f1903953b66624f910feef245ac")
test15.phrase_to_key("64c87cde7e12ecf6704ab95bb1408bef047c22db4cc7491c4271d170a1b213d20b385bc1588d9c7b38f1b39d415665b8a9030c9ec653d75e65f847d8fc1fc440")
test16.phrase_to_key("ea725895aaae8d4c1cf682c1bfd2d358d52ed9f0f0591131b559e2724bb234fca05aa9c02c57407e04ee9dc3b454aa63fbff483a8b11de949624b9f1831a9612")
test17.phrase_to_key("fd579828af3da1d32544ce4db5c73d53fc8acc4ddb1e3b251a31179cdb71e853c56d2fcb11aed39898ce6c34b10b5382772db8796e52837b54468aeb312cfc3d")
test18.phrase_to_key("72be8e052fc4919d2adf28d5306b5474b0069df35b02303de8c1729c9538dbb6fc2d731d5f832193cd9fb6aeecbc469594a70e3dd50811b5067f3b88b28c3e8d")
test19.phrase_to_key("deb5f45449e615feff5640f2e49f933ff51895de3b4381832b3139941c57b59205a42480c52175b6efcffaa58a2503887c1e8b363a707256bdd2b587b46541f5")
test20.phrase_to_key("4cbdff1ca2db800fd61cae72a57475fdc6bab03e441fd63f96dabd1f183ef5b782925f00105f318309a7e9c3ea6967c7801e46c8a58082674c860a37b93eda02")
test21.phrase_to_key("26e975ec644423f4a4c4f4215ef09b4bd7ef924e85d1d17c4cf3f136c2863cf6df0a475045652c57eb5fb41513ca2a2d67722b77e954b4b3fc11f7590449191d")
test22.phrase_to_key("2aaa9242daafcee6aa9d7269f17d4efe271e1b9a529178d7dc139cd18747090bf9d60295d0ce74309a78852a9caadf0af48aae1c6253839624076224374bc63f")
test23.phrase_to_key("7b4a10be9d98e6cba265566db7f136718e1398c71cb581e1b2f464cac1ceedf4f3e274dc270003c670ad8d02c4558b2f8e39edea2775c9e232c7cb798b069e88")
test24.phrase_to_key("01f5bced59dec48e362f2c45b5de68b9fd6c92c6634f44d6d40aab69056506f0e35524a518034ddc1192e1dacd32c1ed3eaa3c3b131c88ed8e7e54c49a5d0998")
