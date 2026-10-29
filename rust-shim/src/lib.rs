//! Rust memory-read shim used by the Python overlay via ctypes.

use windows::Win32::Foundation::{CloseHandle, HANDLE};
use windows::Win32::System::Memory::{
    OpenProcess, ReadProcessMemory, PROCESS_QUERY_INFORMATION, PROCESS_VM_READ,
};

#[no_mangle]
pub unsafe extern "C" fn apex_open(pid: u32) -> isize {
    let h: HANDLE = match OpenProcess(PROCESS_VM_READ | PROCESS_QUERY_INFORMATION, false, pid) {
        Ok(h) => h,
        Err(_) => return 0,
    };
    h.0 as isize
}

#[no_mangle]
pub unsafe extern "C" fn apex_close(handle: isize) {
    if handle != 0 {
        let _ = CloseHandle(HANDLE(handle as _));
    }
}

#[no_mangle]
pub unsafe extern "C" fn apex_read(handle: isize, addr: usize, buf: *mut u8, len: usize) -> usize {
    let mut read = 0usize;
    let ok = ReadProcessMemory(HANDLE(handle as _), addr as _, buf as _, len, Some(&mut read));
    if ok.is_ok() { read } else { 0 }
}