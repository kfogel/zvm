#
# A class which represents the CPU itself, the brain of the virtual
# machine. It ties all the systems together and runs the story.
#
# For the license of this file, please consult the LICENSE file in the
# root directory of this distribution.
#

from zopdecoder import ZOpDecoder

class ZCpuError(Exception):
    "General exception for Zcpu class"

class ZCpuOpcodeOverlap(ZCpuError):
    "Overlapping opcodes registered"

class ZCpuIllegalInstruction(ZCpuError):
    "Illegal instruction encountered"

def declare_opcodes(func, opcodes, version=(1,2,3,4,5)):
    """Helper function used for declaring the a function implements
    some opcodes."""
    if hasattr(func, '_opcodes'):
        raise ZCpuOpcodeOverlap
    func._opcodes = opcodes
    func._opversion = version

def declare_opcode_set(func, base_opcode, n_opcodes,
                       op_increment, version=(1,2,3,4,5)):
    """Helper function used for declaring that a function implements
    several opcodes, spaced out at regular interfals in the opcode space."""
    opcodes = [base_opcode+(i*op_increment) for i in range(0, n_opcodes)]
    return declare_opcodes(func, opcodes, version)

def declare_opcode(func, opcode, version=(1,2,3,4,5)):
    """Helper function used for declaring that a functions implements
    a single opcode."""
    return declare_opcodes(func, (opcode,), version)

def append_opcode(func, opcode):
    """Helper function to add one extra opcode to an already declared
    function."""
    opcodes = func._opcodes
    del func._opcodes
    return declare_opcodes(func, opcodes+[opcode], func._opversion)

class ZCpu(object):

    _opcodes = {}

    def __init__(self, zmem, zopdecoder):
        self._memory = zmem
        self._opdecoder = zopdecoder

    def _get_handler(self, opcode):
        try:
            print "Opcode key: (0x%X, %d)" % (opcode, self._memory.version)
            opcode_func = self._opcodes[(opcode, self._memory.version)]
            print "Handler:", opcode_func
            return getattr(self, opcode_func)
        except KeyError:
            print "Unknown instruction 0x%X" % opcode
            raise ZCpuIllegalInstruction

    def run(self):
        """The Magic Function that takes little bits and bytes, twirls
        them around, and brings the magic to your screen!"""
        print "Execution started"
        while True:
            (opcode, operands) = self._opdecoder.get_next_instruction()
            self._get_handler(opcode)(*operands)
            print

    ##
    ## Opcode implementation functions start here.
    ##

    ## 2OP opcodes (opcodes 1-127 and 192-223)
    def op_je(*args):
        """"""
    declare_opcode_set(op_je, 0x01, 4, 0x20)
    append_opcode(op_je, 0xC1)

    def op_jl(*args):
        """"""
    declare_opcode_set(op_jl, 0x02, 4, 0x20)
    append_opcode(op_jl, 0xC2)

    def op_jg(*args):
        """"""
    declare_opcode_set(op_jg, 0x03, 4, 0x20)
    append_opcode(op_jg, 0xC3)

    def op_dec_chk(*args):
        """"""
    declare_opcode_set(op_dec_chk, 0x04, 4, 0x20)
    append_opcode(op_dec_chk, 0xC4)

    def op_inc_chk(*args):
        """"""
    declare_opcode_set(op_inc_chk, 0x05, 4, 0x20)
    append_opcode(op_inc_chk, 0xC5)

    def op_jin(*args):
        """"""
    declare_opcode_set(op_jin, 0x06, 4, 0x20)
    append_opcode(op_jin, 0xC6)

    def op_test(*args):
        """"""
    declare_opcode_set(op_test, 0x07, 4, 0x20)
    append_opcode(op_jin, 0xC7)

    def op_or(*args):
        """"""
    declare_opcode_set(op_or, 0x08, 4, 0x20)
    append_opcode(op_or, 0xC8)

    def op_and(*args):
        """"""
    declare_opcode_set(op_and, 0x09, 4, 0x20)
    append_opcode(op_and, 0xC9)

    def op_test_attr(*args):
        """"""
    declare_opcode_set(op_test_attr, 0x0A, 4, 0x20)
    append_opcode(op_test_attr, 0xCA)

    def op_set_attr(*args):
        """"""
    declare_opcode_set(op_set_attr, 0x0B, 4, 0x20)
    append_opcode(op_set_attr, 0xCB)

    def op_clear_attr(*args):
        """"""
    declare_opcode_set(op_clear_attr, 0x0C, 4, 0x20)
    append_opcode(op_clear_attr, 0xCC)

    def op_store(*args):
        """"""
    declare_opcode_set(op_store, 0x0D, 4, 0x20)
    append_opcode(op_store, 0xCD)

    def op_insert_obj(*args):
        """"""
    declare_opcode_set(op_insert_obj, 0x0E, 4, 0x20)
    append_opcode(op_insert_obj, 0xCE)

    def op_loadw(*args):
        """"""
    declare_opcode_set(op_loadw, 0x0F, 4, 0x20)
    append_opcode(op_loadw, 0xCF)

    def op_loadb(*args):
        """"""
    declare_opcode_set(op_loadb, 0x10, 4, 0x20)
    append_opcode(op_loadb, 0xD0)

    def op_get_prop(*args):
        """"""
    declare_opcode_set(op_get_prop, 0x11, 4, 0x20)
    append_opcode(op_get_prop, 0xD1)

    def op_get_prop_addr(*args):
        """"""
    declare_opcode_set(op_get_prop_addr, 0x12, 4, 0x20)
    append_opcode(op_get_prop_addr, 0xD2)

    def op_get_next_prop(*args):
        """"""
    declare_opcode_set(op_get_next_prop, 0x13, 4, 0x20)
    append_opcode(op_get_next_prop, 0xD3)

    def op_add(*args):
        """"""
    declare_opcode_set(op_add, 0x14, 4, 0x20)
    append_opcode(op_add, 0xD4)

    def op_sub(*args):
        """"""
    declare_opcode_set(op_sub, 0x15, 4, 0x20)
    append_opcode(op_sub, 0xD5)

    def op_mul(*args):
        """"""
    declare_opcode_set(op_mul, 0x16, 4, 0x20)
    append_opcode(op_mul, 0xD6)

    def op_div(*args):
        """"""
    declare_opcode_set(op_div, 0x17, 4, 0x20)
    append_opcode(op_div, 0xD7)

    def op_mod(*args):
        """"""
    declare_opcode_set(op_mod, 0x18, 4, 0x20)
    append_opcode(op_mod, 0xD8)

    def op_call_2s(*args):
        """"""
    declare_opcode_set(op_call_2s, 0x19, 4, 0x20, version=(4,5))
    append_opcode(op_call_2s, 0xD9)

    def op_call_2n(*args):
        """"""
    declare_opcode_set(op_call_2n, 0x1A, 4, 0x20, version=(5,))
    append_opcode(op_call_2n, 0xDA)

    def op_set_colour(*args):
        """"""
    declare_opcode_set(op_set_colour, 0x1B, 4, 0x20, version=(5,))
    append_opcode(op_set_colour, 0xDB)

    def op_throw(*args):
        """"""
    declare_opcode_set(op_throw, 0x1C, 4, 0x20, version=(5,))
    append_opcode(op_throw, 0xDC)

    ## 1OP opcodes (opcodes 128-175)

    def op_jz(*args):
        """"""
    declare_opcode_set(op_jz, 0x80, 2, 0x10)

    def op_get_sibling(*args):
        """"""
    declare_opcode_set(op_get_sibling, 0x81, 2, 0x10)

    def op_get_child(*args):
        """"""
    declare_opcode_set(op_get_child, 0x82, 2, 0x10)

    def op_get_parent(*args):
        """"""
    declare_opcode_set(op_get_parent, 0x83, 2, 0x10)

    def op_get_prop_len(*args):
        """"""
    declare_opcode_set(op_get_prop_len, 0x84, 2, 0x10)

    def op_inc(*args):
        """"""
    declare_opcode_set(op_inc, 0x85, 2, 0x10)

    def op_dec(*args):
        """"""
    declare_opcode_set(op_dec, 0x86, 2, 0x10)

    def op_print_addr(*args):
        """"""
    declare_opcode_set(op_print_addr, 0x87, 2, 0x10)

    def op_call_1s(*args):
        """"""
    declare_opcode_set(op_call_1s, 0x88, 2, 0x10, version=(4,5))

    def op_remove_obj(*args):
        """"""
    declare_opcode_set(op_remove_obj, 0x89, 2, 0x10)

    def op_print_obj(*args):
        """"""
    declare_opcode_set(op_print_obj, 0x8A, 2, 0x10)

    def op_ret(*args):
        """"""
    declare_opcode_set(op_ret, 0x8B, 2, 0x10)

    def op_jump(*args):
        """"""
    declare_opcode_set(op_jump, 0x8C, 2, 0x10)

    def op_print_paddr(*args):
        """"""
    declare_opcode_set(op_print_paddr, 0x8D, 2, 0x10)

    def op_load(*args):
        """"""
    declare_opcode_set(op_load, 0x8E, 2, 0x10)

    def op_not(*args):
        """"""
    declare_opcode_set(op_not, 0x8F, 2, 0x10, version=(1,2,3,4))

    def op_call_1n(*args):
        """"""
    declare_opcode_set(op_call_1n, 0x8F, 2, 0x10, version=(5,))

    ## 0OP opcodes (opcodes 176-191)

    def op_rtrue(*args):
        """"""
    declare_opcode(op_rtrue, 0xB0)

    def op_rfalse(*args):
        """"""
    declare_opcode(op_rfalse, 0xB1)

    def op_print(*args):
        """"""
    declare_opcode(op_print, 0xB2)

    def op_print_ret(*args):
        """"""
    declare_opcode(op_print_ret, 0xB3)

    def op_nop(*args):
        """"""
    declare_opcode(op_nop, 0xB4)

    def op_save(*args):
        """"""
    declare_opcode(op_save, 0xB5, version=(1,2,3))

    def op_save_v4(*args):
        """"""
    declare_opcode(op_save_v4, 0xB5, version=(4,))

    def op_restore(*args):
        """"""
    declare_opcode(op_restore, 0xB6, version=(1,2,3))

    def op_restore_v4(*args):
        """"""
    declare_opcode(op_restore_v4, 0xB6, version=(4,))

    def op_restart(*args):
        """"""
    declare_opcode(op_restart, 0xB7)

    def op_ret_popped(*args):
        """"""
    declare_opcode(op_ret_popped, 0xB8)

    def op_pop(*args):
        """"""
    declare_opcode(op_pop, 0xB9, version=(1,2,3,4))

    def op_catch(*args):
        """"""
    declare_opcode(op_catch, 0xB9, version=(5,))

    def op_quit(*args):
        """"""
    declare_opcode(op_quit, 0xBA)

    def op_new_line(*args):
        """"""
    declare_opcode(op_new_line, 0xBB)

    def op_show_status(*args):
        """"""
    declare_opcode(op_show_status, 0xBC, version=(3,))

    def op_verify(*args):
        """"""
    declare_opcode(op_verify, 0xBD)

    def op_piracy(*args):
        """"""
    declare_opcode(op_piracy, 0xBF)

    ## VAR opcodes (opcodes 224-255)

    def op_call(*args):
        """"""
    declare_opcode(op_call, 0xE0, version=(1,2,3))

    def op_call_vs(*args):
        """"""
    declare_opcode(op_call_vs, 0xE0, version=(4,5))

    def op_storew(*args):
        """"""
    declare_opcode(op_storew, 0xE1)

    def op_storeb(*args):
        """"""
    declare_opcode(op_storeb, 0xE2)

    def op_put_prop(*args):
        """"""
    declare_opcode(op_put_prop, 0xE3)

    def op_sread(*args):
        """"""
    declare_opcode(op_sread, 0xE4, version=(1,2,3))

    def op_sread_v4(*args):
        """"""
    declare_opcode(op_sread_v4, 0xE4, version=(4,))

    def op_aread(*args):
        """"""
    declare_opcode(op_aread, 0xE4, version=(5,))

    def op_print_char(*args):
        """"""
    declare_opcode(op_print_char, 0xE5)

    def op_print_num(*args):
        """"""
    declare_opcode(op_print_num, 0xE6)

    def op_random(*args):
        """"""
    declare_opcode(op_random, 0xE7)

    def op_push(*args):
        """"""
    declare_opcode(op_push, 0xE8)

    def op_pull(*args):
        """"""
    declare_opcode(op_pull, 0xE9)

    def op_split_window(*args):
        """"""
    declare_opcode(op_split_window, 0xEA, version=(3,4,5))

    def op_set_window(*args):
        """"""
    declare_opcode(op_set_window, 0xEB, version=(3,4,5))

    def op_call_vs2(*args):
        """"""
    declare_opcode(op_call_vs2, 0xEC, version=(4,5))

    def op_erase_window(*args):
        """"""
    declare_opcode(op_erase_window, 0xED, version=(4,5))

    def op_erase_line(*args):
        """"""
    declare_opcode(op_erase_line, 0xEE, version=(4,5))

    def op_set_cursor(*args):
        """"""
    declare_opcode(op_set_cursor, 0xEF, version=(4,5))

    def op_get_cursor(*args):
        """"""
    declare_opcode(op_get_cursor, 0xF0, version=(4,5))

    def op_set_text_style(*args):
        """"""
    declare_opcode(op_set_text_style, 0xF1, version=(4,5))

    def op_buffer_mode(*args):
        """"""
    declare_opcode(op_buffer_mode, 0xF2, version=(4,5))

    def op_output_stream(*args):
        """"""
    declare_opcode(op_output_stream, 0xF3, version=(3,4))

    def op_output_stream_v5(*args):
        """"""
    declare_opcode(op_output_stream_v5, 0xF3, version=(5,))

    def op_input_stream(*args):
        """"""
    declare_opcode(op_input_stream, 0xF4, version=(3,4,5))

    # This one may have been used prematurely in v3 stories. Keep an
    # eye out for it if we ever get bug reports.
    def op_sound_effect(*args):
        """"""
    declare_opcode(op_sound_effect, 0xF5, version=(5,))

    def op_read_char(*args):
        """"""
    declare_opcode(op_read_char, 0xF6, version=(4,5))

    def op_scan_table(*args):
        """"""
    declare_opcode(op_scan_table, 0xF7, version=(4,5))

    def op_not_v5(*args):
        """"""
    declare_opcode(op_not_v5, 0xF8, version=(5,))

    def op_call_vn(*args):
        """"""
    declare_opcode(op_call_vn, 0xF9, version=(5,))

    def op_call_vn2(*args):
        """"""
    declare_opcode(op_call_vn2, 0xFA, version=(5,))

    def op_tokenize(*args):
        """"""
    declare_opcode(op_tokenize, 0xFB, version=(5,))

    def op_encode_text(*args):
        """"""
    declare_opcode(op_encode_text, 0xFC, version=(5,))

    def op_copy_table(*args):
        """"""
    declare_opcode(op_copy_table, 0xFD, version=(5,))

    def op_print_table(*args):
        """"""
    declare_opcode(op_print_table, 0xFE, version=(5,))

    def op_check_arg_count(*args):
        """"""
    declare_opcode(op_check_arg_count, 0xFF, version=(5,))

    ## EXT opcodes (opcodes 256-284)

    def op_save(*args):
        """"""
    declare_opcode(op_save, 0x100, version=(5,))

    def op_restore(*args):
        """"""
    declare_opcode(op_restore, 0x101, version=(5,))

    def op_log_shift(*args):
        """"""
    declare_opcode(op_log_shift, 0x102, version=(5,))

    def op_art_shift(*args):
        """"""
    declare_opcode(op_art_shift, 0x103, version=(5,))

    def op_set_font(*args):
        """"""
    declare_opcode(op_set_font, 0x104, version=(5,))

    def op_save_undo(*args):
        """"""
    declare_opcode(op_save_undo, 0x109, version=(5,))

    def op_restore_undo(*args):
        """"""
    declare_opcode(op_restore_undo, 0x10A, version=(5,))

    def op_print_unicode(*args):
        """"""
    declare_opcode(op_print_unicode, 0x10B, version=(5,))

    def op_check_unicode(*args):
        """"""
    declare_opcode(op_check_unicode, 0x10C, version=(5,))


    # This is the "automagic" opcode handler registration system.
    # After each function that is an opcode handler, we assign the
    # function object an _opcode attribute, giving the numeric opcode
    # the function implements.
    #
    # Then, the following code iterates back over all items in the
    # class, and registers all objects with that attribute in the
    # _opcodes dictionary.
    #
    # Then, at runtime, the _get_handler method can be invoked to
    # retrieve the function implementing a given opcode.  Pretty cool
    # voodoo if you ask me.
    for k,v in vars().items():
        if hasattr(v, "_opcodes"):
            for opc in v._opcodes:
                for ver in v._opversion:
                    opkey = (opc, ver)

                    if opkey in _opcodes.keys():
                        print "Opcode key",opkey,"already defined"
                        raise ZCpuOpcodeOverlap

                    _opcodes[opkey] = k
