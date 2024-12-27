
from pages.interactions_page import SortablePage, SelectablePage, ResizeablePage, DroppablePage, DraggablePage


class TestInteractions:

    class TestSortablePage:

        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            # print(list_before, list_after)
            # print(grid_before, grid_after)
            assert list_before != list_after, "The order of the list has not been changed"
            assert grid_before != grid_after, "The order of the grid has not been changed"


    class TestSelectablePage:

        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            # print(item_list)
            # print(item_grid)
            assert item_list > 0, "No elements were selected"
            assert item_grid > 0, "No elements were selected"



    class TestResizeablePage:

        def test_resizeable(self, driver):
            resizeable_page = ResizeablePage(driver, "https://demoqa.com/resizable")
            resizeable_page.open()
            max_box, min_box = resizeable_page.change_size_resizeable_box()
            max_resize, min_resize = resizeable_page.change_size_resizeable()
            # print(max_box, min_box)
            # print(max_resize, min_resize)
            assert ('500px', '300px') == max_box, "Maximum size not equal to '500px', '300px'"
            assert ('150px', '150px') == min_box, "Minimum size not equal to '150px', '150px'"
            assert min_resize != max_resize, "Resizeable has not been changed"

    class TestDroppablePage:

        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            text = droppable_page.drop_simple()
            # print(text)
            assert text == "Dropped!", "The elements has not been dropped"

        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_accept, accept = droppable_page.drop_accept()
            # print(not_accept)
            # print(accept)
            assert not_accept == 'Drop here', 'The dropped element has been accepted'
            assert accept     == 'Dropped!', 'The dropped element has not been accepted'


        def test_prevent_propagation(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.drop_prevent_propogation()
            # print(not_greedy)
            # print(not_greedy_inner)
            # print(greedy)
            # print(greedy_inner)
            assert not_greedy       == 'Dropped!', 'Text of the element has not been changed'
            assert not_greedy_inner == 'Dropped!', 'Text of the element has not been changed'
            assert greedy           == 'Outer droppable', 'Text of the element has been changed'
            assert greedy_inner     == 'Dropped!', 'Text of the element has not been changed'




        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            will_after_move, will_after_revert = droppable_page.drop_revert_draggable('will_revert')
            # print(will_after_move)
            # print(will_after_revert)
            not_will_after_move, not_will_after_revert = droppable_page.drop_revert_draggable('not_will_revert')
            # print(not_will_after_move)
            # print(not_will_after_revert)
            assert will_after_move != will_after_revert, 'The element has not revert'
            assert not_will_after_move == not_will_after_revert, 'The element has revert'

    class TestDraggablePage:

        def test_simple_draggable(self, driver):
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()
            before, after = draggable_page.simple_drag_box()
            # print(before)
            # print(after)
            assert before != after

        def test_axis_draggable_restricted(self, driver):
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()
            top_x, left_x = draggable_page.axis_restricted_x()
            top_y, left_y = draggable_page.axis_restricted_y()
            # print(top_x)
            # print(left_x)
            # print(top_y)
            # print(left_y)
            assert top_x[0][0] == top_x[1][0] and int(top_x[1][0]) == 0, 'The box position has not changed or there has been a shift in the y-axis'
            assert left_x[0][0] != left_x[1][0] and int(left_x[1][0]) != 0, 'The box position has not changed or there has been a shift in the y-axis'
            assert top_y[0][0] != top_y[1][0] and int(top_y[1][0]) != 0, 'The box position has not changed or there has been a shift in the x-axis'
            assert left_y[0][0] == left_y[1][0] and int(left_y[1][0]) == 0, 'The box position has not changed or there has been a shift in the x-axis'










